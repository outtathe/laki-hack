from aiogram import Bot, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ContentType
import requests

from . import config as config
from src.keyboards import web_app_button

router = Router()


@router.message(Command(commands=['start']))
async def command_start_bot(
    message: Message, 
    command: CommandObject, 
    bot: Bot
):
    
    await message.answer(f'Привет! Нажми /reg чтобы подписаться на уведомления')


@router.message(Command(commands=['reg']))
async def command_reg_bot(
    message: Message, 
    command: CommandObject, 
    bot: Bot
):
    async def check_user(tg_name, user_id):
        data = {'tg_name': tg_name, 'user_id': user_id}
        responce = requests.post(f'https://{config.APP_URL}/backend/bot/check_user_reg', json=data)
        if responce.status_code == 200:
            return responce.json()
        return None
    
    username = message.from_user.username
    tg_id = message.from_user.id

    res = await check_user(username, tg_id)
    if res:
        data = res['data']
        await message.answer(f'{data}')
    else:
        await message.answer(f'{username} отсутствует в системе!')


@router.message(Command(commands=['me']))
async def command_profile_bot(
    message: Message, 
    command: CommandObject, 
    bot: Bot
):
    async def get_profile(tg_name, user_id):
        data = {'tg_name': tg_name, 'user_id': user_id}
        responce = requests.post(f'https://{config.APP_URL}/backend/bot/profile', json=data)
        if responce.status_code == 200:
            return responce.json()
        return None
    
    username = message.from_user.username
    tg_id = message.from_user.id

    res = await get_profile(username, tg_id)
    if res:
        data = res['data']
        await message.answer(f'{data}')
    else:
        await message.answer(f'{username} отсутствует в системе!')


# @router.message(content_types=[ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER])
# async def save_new_chat_member(message: Message):
#     async def save_chat_member(chat_id, user_id):
#         data = {'chat_id': chat_id, 'user_id': user_id}
#         responce = requests.post(f'https/{config.APP_URL}/backend/bot/member', data=data)
#         if responce.status_code == 200:
#             return responce.json()
#         return None

#     chat_id = message.chat.id
#     user_id = message.from_user.id

#     await save_chat_member(chat_id, user_id)


# @router.message(Command(commands=['hack']))
# async def test(
#     message: Message, 
#     command: CommandObject,
#     bot: Bot
# ):
#     await message.answer(
#         'Открой веб апп!', 
#         reply_markup=web_app_button
#     )

