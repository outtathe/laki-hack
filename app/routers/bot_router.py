from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas.user_schemas import BotCheck, BotSendMsg # BotSaveChat
from services.user_service import bot_check_user, bot_get_profile, bot_send_msg # bot_save_member
# from services.auth_utils import get_current_user
# from requests import post
import json

bot_router = APIRouter()


@bot_router.post('/check_user_reg')
async def route_bot_check(BotCheck: BotCheck) -> JSONResponse:
    try:
        await bot_check_user(BotCheck.tg_name, BotCheck.user_id)
        data = {
            'data': 'Вы успешно привязали бота!',
        }
        return JSONResponse(data, status_code=status.HTTP_200_OK)

    except Exception as e:
        return JSONResponse({'exc': e}, status_code=status.HTTP_400_BAD_REQUEST)


@bot_router.post('/profile')
async def route_bot_get_profile(BotCheck: BotCheck) -> JSONResponse:
    profile = await bot_get_profile(BotCheck.tg_name, BotCheck.user_id)
    info = f'Привет {profile.name}!\nТвои компетенции:\n{jsonable_encoder(profile.competence_groups)}'
    data = {
        'data': info,
    }
    return JSONResponse(data, status_code=status.HTTP_200_OK)


@bot_router.post('/send_msg')
async def route_bot_send_msg(BotSendMsg: BotSendMsg) -> JSONResponse:
    info = await bot_send_msg(BotSendMsg.chat_id, BotSendMsg.text)
    data = {
        'msg': 'message successfully send',
        'info': info
    }
    return JSONResponse(data, status_code=status.HTTP_200_OK)


# @bot_router.post('/member')
# async def route_bot_save_member(BotSendMsg: BotSaveChat) -> JSONResponse:
#     info = await bot_save_member(BotSaveChat.chat_id, BotSaveChat.user_id)
#     data = {
#         'msg': 'member successfully save',
#     }
#     return JSONResponse(data, status_code=status.HTTP_200_OK)

