from sqlalchemy import delete, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from .db import async_session
from .utils import row_list_to_dict_list, row_to_dict
from schemas.user_schemas import NewUserData, HackData, TeamData, CompetencesData
from .models.user_models import Users, Competences, CompetenceGroups, Teams, UserTeams, Hackathon


async def reg_user(login: str, password: str) -> int | None:
    session: AsyncSession
    async with async_session() as session:
        check = await session.execute(
            select(
                Users.login
            ).where(
                Users.login == login
            )
        )
        check = check.scalar_one_or_none()
        if check is not None:
            raise HTTPException(
                detail='login already exist',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        new_user = Users(
            login=login,
            password=password
        )
        session.add(new_user)
        await session.commit()

        return new_user.id


async def get_user_by_id(id_user: int):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.id == id_user
            )
        )
        user = user.scalar_one_or_none()
        return user


async def get_user_by_login(login: str):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.login == login
            )
        )
        user = user.scalar_one_or_none()
        return user


async def update_user(id_user: int, new_data: NewUserData):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.id == id_user
            )
        ) # .scalar_one()
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'id={id_user} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        data_dict = {key: val for key, val in new_data if val is not None and key not in 'competence_list'}
        await user.update(**data_dict)
        user.competence_groups = await update_competence_group(session, new_data.competence_list)
        await session.commit()


async def get_all_competences():
    session: AsyncSession
    async with async_session() as session:
        competences = await session.execute( 
            select(
                Competences
            )
        )
        competences = competences.scalars().all()

        return competences


async def create_competences(comp_data: list[CompetencesData]):
    session: AsyncSession
    async with async_session() as session:
        id_list = []
        for comp in comp_data:
            new_comp = Competences(**(comp.dict()))
            session.add(new_comp)
            await session.flush()
            id_list.append(new_comp.id)
        await session.commit()
        return id_list


async def update_competence_group(session: AsyncSession, comp_list: list[int] | None):
    if comp_list is None:
        return None
    
    comp_len = len(comp_list)
    competence_group = None

    comp_chek = await session.execute(
        select(
            Competences
        ).where(
            Competences.id.in_(comp_list)
        )
    )
    chek_len = len(comp_chek.scalars().all())
    if chek_len != comp_len:
        raise HTTPException(
                detail=f'some competences id from {comp_list} does not exist',
                status_code=status.HTTP_400_BAD_REQUEST
            )
    
    competence_group_list = await session.execute(
        select(
            CompetenceGroups
        ).join(
            CompetenceGroups.competences
        ).where(
            Competences.id.in_(comp_list)
        ).group_by(
            CompetenceGroups.id
        ).having(
            func.count(Competences.id) == comp_len
        )
    )
    competence_group_list = competence_group_list.scalars().all()

    need_create = True

    # SOME SHITY HACK
    if competence_group_list:
        for comp_group in competence_group_list:
            if set(comp_list) == set([cm.id for cm in comp_group.competences]):
                competence_group = comp_group
                need_create = False
                break

    if need_create:
        competences = await session.execute(
            select(
                Competences
            ).where(
                Competences.id.in_(comp_list)
            )
        )
        competences = competences.scalars().all()

        competence_group = CompetenceGroups(competences=competences)
        session.add(competence_group)
        await session.commit()

    return competence_group
    

async def create_hackathone(hack_data: HackData):
    session: AsyncSession
    async with async_session() as session:
        hack = Hackathon(
            **(hack_data.dict())
        )
        # ПОСМОТРЕТЬ КОНВЕРТАЦИЮ ПИДАНТИК В SQLALCHEMY

        if hack is None:
            raise HTTPException(
                detail='Error',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        session.add(hack)
        await session.commit()
        return hack.id


async def update_hackathone(id_hack: int, new_hack_data: HackData):
    session: AsyncSession
    async with async_session() as session:
        hack = await session.execute(
            select(
                Hackathon
            ).where(
                Hackathon.id == id_hack
            )
        )
        hack = hack.scalar_one_or_none()
        if hack is None:
            raise HTTPException(
                detail=f'id={id_hack} does not exist in hackthone table',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        update_data = {key: val for key, val in new_hack_data if val is not None}
        await hack.update(**update_data)
        await session.commit()


async def get_team(id_team: int):
    session: AsyncSession
    async with async_session() as session:
        team = await session.execute(
            select(
                Teams
            ).where(
                Teams.id == id_team
            )
        )
        team = team.scalar_one_or_none()
        return team


async def create_team(id_user, id_hack, new_team: TeamData):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.id == id_user
            )
        )
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'id={id_user} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        user_team = UserTeams()
        await session.flush()
        user_team.user.append(user)
        # TODO сделать добавление роли менеджера
        user_team.competence_groups = await update_competence_group(session, [1])

        team = Teams(**(new_team.dict()))
        # session.add(team)
        # await session.flush()

        team.users.append(user_team)
        session.add(team)
        await session.flush()


        hack = await session.execute(
            select(
                Hackathon
            ).where(
                Hackathon.id == id_hack
            )
        )
        hack = hack.scalar_one_or_none()
        
        hack.teams.append(team)
        await session.commit()

        return team.id


async def update_team(id_team: int, new_team: TeamData):
    session: AsyncSession
    async with async_session() as session:
        team = await session.execute(
            select(
                Teams
            ).where(
                Teams.id == id_team
            )
        )
        team = team.scalar_one_or_none()
        if team is None:
            raise HTTPException(
                detail=f'id={id_team} does not exist in teams table',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        new_data = {key: val for key, val in new_team if val is not None}
        await team.update(**new_data)
        await session.commit()


async def join_user_to_team(id_team: int, id_user: int):
    session: AsyncSession
    async with async_session() as session:
        team = await session.execute(
            select(
                Teams
            ).where(
                Teams.id == id_team
            )
        )
        team = team.scalar_one_or_none()
        if team is None:
            raise HTTPException(
                detail=f'id={id_team} does not exist in teams table',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        user = await session.execute(
            select(
                Users
            ).where(
                Users.id == id_user
            )
        )
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'id={user} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        user_team = UserTeams(
            id_user=id_user,
            # TODO сделать добавление роли менеджера
            # id_competence_group = await update_competence_group([1])
        )

        team.users.append(user_team)
        await session.commit()


async def update_user_team_competence(id_team: int, id_user: int, new_comp: list[int]):
    session: AsyncSession
    async with async_session() as session:    
        user_team = await session.execute(
            select(
                UserTeams
            ).where(
                UserTeams.id_user == id_user,
                UserTeams.id_team == id_team
            )
        )
        user_team = user_team.scalar_one_or_none()
        if user_team is None:
            raise HTTPException(
                detail=f'{id_user=} or {id_team} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        user_team.competence_groups = await update_competence_group(session, new_comp)
        await session.commit()


async def delete_user_from_team(id_team: int, id_user: int):
    session: AsyncSession
    async with async_session() as session:
        team = await session.execute(
            select(
                Teams
            ).where(
                Teams.id == id_team
            )
        )
        team = team.scalar_one_or_none()
        if team is None:
            raise HTTPException(
                detail=f'id={id_team} does not exist in teams table',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        user_team = await session.execute(
            select(
                UserTeams
            ).where(
                UserTeams.id_user == id_user
            )
        )
        user_team = user_team.scalar_one_or_none()
        if user_team is None:
            raise HTTPException(
                detail=f'id={id_user} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        await session.delete(user_team)
        await session.commit()


async def bot_check_user(tg_name: str, user_id: int):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.telegram == tg_name
            )
        )
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'{tg_name=} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            ) 

        user.tg_id = user_id
        await session.commit()


async def bot_get_profile(tg_name: str, user_id: int) -> Users:
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.telegram == tg_name,
                Users.tg_id == user_id,
            )
        )
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'{tg_name=}&{user_id=} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            ) 

        return user


async def bot_send_msg(chat_id: int) -> bool:
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.tg_id == chat_id,
            )
        )
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                detail=f'user_id={chat_id} does not exist in users table',
                status_code=status.HTTP_400_BAD_REQUEST
            ) 

        return True
