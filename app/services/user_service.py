from fastapi import HTTPException, status
import requests

from schemas.user_schemas import NewUserData, CompetencesData, HackData, TeamData
import database.user_db as db
import services.auth_utils as auth
from params.confing import BOT_URL


# TODO Возможно надо достать логику из auth.reg_user() и auth.auth_user()
async def registration_user(login: str, password: str) -> int | None:
    id_user = await auth.reg_user(login, password)
    # access_token = await auth.create_access_token({'sub': login})
    
    user_data = {
        # 'access_token': access_token,
        # 'token_type': 'bearer',
        'id_user': id_user
    }

    return user_data


async def login_user(login, password) -> dict | None:
    user = await auth.auth_user(login, password)
    # access_token = await auth.create_access_token({'sub': user.login})

    user_data = {
        # 'access_token': access_token,
        # 'token_type': 'bearer',
        'id_user': user.id,
    }
        
    return user_data


async def update_user_info(id_user: int, user_data: NewUserData):
    await db.update_user(id_user, user_data)
    return


async def get_all_competences():
    all_competences = await db.get_all_competences()
    return all_competences


async def create_competences(comp_data: list[CompetencesData]):
    new_comp_id_list = await db.create_competences(comp_data)
    return new_comp_id_list


async def create_hackathone(hack_data: HackData):
    new_hack_id = await db.create_hackathone(hack_data)
    return new_hack_id


async def update_hackathone(id_hack: int, new_hack_data: HackData):
    await db.update_hackathone(id_hack, new_hack_data)


async def get_team(id_team: int):
    team = await db.get_team(id_team)
    return team


async def create_new_team(id_user, id_hack, new_team: TeamData):
    new_team_id = await db.create_team(id_user, id_hack, new_team)
    return new_team_id


async def update_team(id_team: int, new_team: TeamData):
    await db.update_team(id_team, new_team)


async def join_user_to_team(id_team: int, id_user: int):
    await db.join_user_to_team(id_team, id_user)


async def update_user_team_competence(id_team: int, id_user: int, new_comp: list[int]):
    await db.update_user_team_competence(id_team, id_user, new_comp)


async def delete_user_from_team(id_team: int, id_user: int):
    await db.delete_user_from_team(id_team, id_user)


async def bot_check_user(tg_name: str, user_id: int):
    await db.bot_check_user(tg_name, user_id)
    

async def bot_get_profile(tg_name: str, user_id: int):
    profile = await db.bot_get_profile(tg_name, user_id)
    return profile


async def bot_send_msg(chat_id: int, msg: str):
    check = await db.bot_send_msg(chat_id)
    if check:
        data = {'chat_id': chat_id, 'text': msg}
        res = requests.post(f'https://{BOT_URL}/api/send_msg', json=data)
        if res.status_code == 200:
            res = res.json()
            return res['detail']
    else:
        raise HTTPException(
            detail=f'some error while request',
            status_code=status.HTTP_400_BAD_REQUEST
        ) 


# async def bot_save_member(chat_id: int, user_id: int):
#     await db.bot_save_member(chat_id, user_id)
