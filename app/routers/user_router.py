from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from schemas.user_schemas import UserRegistration, UserLoginOut, NewUserData, ChatInput
from services.user_service import *
from services.auth_utils import get_current_user
from requests import post
import json

user_router = APIRouter()


@user_router.post('/chat')
async def route_chat(chat_input: ChatInput) -> JSONResponse:    
    url = "https://llm.api.cloud.yandex.net/llm/v1alpha/chat"
    headers = {
    'Authorization': 'Api-Key AQVN3htkeAe3DUrEbA9VMLnzsOSITb_eCu4EbRhG',
        'x-folder-id': 'b1gir4mg1slbpvl4bb9r'
    }
    data = {
        "model": chat_input.model,
        "generationOptions": {
            "partialResults": chat_input.partial_results,
            "temperature": chat_input.temperature,
            "maxTokens": chat_input.max_tokens
        },
        "messages": [
            {
            "role": chat_input.role,
            "text": chat_input.text
            }
        ],
        "instructionText": chat_input.instruction_text
    }
    data = json.dumps(data)
    response = post(url, data=data, headers=headers)
    response = json.loads(response.text)
    return JSONResponse(response, status_code=status.HTTP_200_OK)


@user_router.post('/registration', response_model=UserLoginOut)
async def route_registration(user_reg: UserRegistration) -> JSONResponse:
    user_data = await registration_user(user_reg.login, user_reg.password)
    
    data = {
        'msg': 'user successfully registered',
        'id_user': user_data['id_user'],
        # 'access_token ': user_data['access_token'],
        # 'token_type': user_data['token_type']

    }
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.post('/login')
async def route_login(login_form: OAuth2PasswordRequestForm = Depends()):
    login_form.username = login_form.username.lower()
    user_data = await login_user(login_form.username, login_form.password)
    data = {
        'msg': 'user successfully auth',
        'id_user': user_data['id_user'],
        # 'access_token ': user_data['access_token'],
        # 'token_type': user_data['token_type']
    }
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.get('/user')
async def route_get_user(user: dict = Depends(get_current_user)):
    data = {
        'user': jsonable_encoder(user)
    }
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.post('/user')
async def route_update_user(id_user: int, new_user_data: NewUserData, user = Depends(get_current_user)):
    await update_user_info(id_user, new_user_data)
    data = {
        'msg': 'user successfully updated',
        'id_user': id_user
    }

    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.get('/competences')
async def route_get_all_competences(user = Depends(get_current_user)):
    all_comp = await get_all_competences()
    data = {
        'competences_list': jsonable_encoder(all_comp)
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.post('/competences')
async def route_create_competences(comp_data: list[CompetencesData], user = Depends(get_current_user)):
    new_comp_id_list = await create_competences(comp_data)
    data = {
        'msg': 'competences successfully created',
        'id_competence_list': new_comp_id_list
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.post('/hackathone')
async def route_create_hackathone(hack_data: HackData, user = Depends(get_current_user)):
    new_hack_id = await create_hackathone(hack_data)
    data = {
        'msg': 'hackathone successfully created',
        'id_hackathone': new_hack_id
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.patch('/hackathone')
async def route_update_hackathone(id_hack: int, new_hack_data: HackData, user = Depends(get_current_user)):
    await update_hackathone(id_hack, new_hack_data)
    data = {
        'msg': 'hackathone successfully updated',
        'id_hackathone': id_hack
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)

# TODO проверить приходят ли члены команды
@user_router.get('/team')
async def route_get_team(id_team: int, user = Depends(get_current_user)):
    team = await get_team(id_team)
    data = {
        'team': jsonable_encoder(team)
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.post('/team')
async def route_create_new_team(id_user: int, id_hack: int, new_team: TeamData, user = Depends(get_current_user)):
    new_team_id = await create_new_team(id_user, id_hack, new_team)
    data = {
        'msg': 'team successfully created',
        'id_team': new_team_id
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.patch('/team')
async def route_update_team(id_team: int, new_team: TeamData, user = Depends(get_current_user)):
    await update_team(id_team, new_team)
    data = {
        'msg': 'team successfully updated',
        'id_team': id_team
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)

# TODO Добавить?
# @user_router.GET('/team/users') - возврат списка членов команды

@user_router.post('/team/users')
async def route_join_user_to_team(id_team: int, id_user: int, user = Depends(get_current_user)):
    await join_user_to_team(id_team, id_user)
    data = {
        'msg': 'user successfully joined team',
        'id_team': id_team,
        'id_user': id_user
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.patch('/team/user/competence')
async def route_update_user_team_competence(id_team: int, id_user: int, new_comp: list[int], user = Depends(get_current_user)):
    await update_user_team_competence(id_team, id_user, new_comp)
    data = {
        'msg': 'user teams competence successfully updated',
        'id_team': id_team,
        'id_user': id_user
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@user_router.delete('/team/user/competence')
async def route_delete_user_from_team(id_team: int, id_user: int, user = Depends(get_current_user)):
    await delete_user_from_team(id_team, id_user)
    data = {
        'msg': 'user successfully deleted from team',
        'id_team': id_team,
        'id_user': id_user
    }  
    return JSONResponse(data, status_code=status.HTTP_200_OK)
