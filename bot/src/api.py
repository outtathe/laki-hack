from aiohttp.web_request import Request
from . import config as config
from . import keyboards as keyboards
from aiogram import Bot
from aiohttp.web_response import json_response
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiogram.exceptions import TelegramBadRequest


async def send_message(request: Request):
    bot: Bot = request.app['bot']

    data = await request.json()
    chat_id = data.get('chat_id')
    text = data.get('text')

    await bot.send_message(
        int(chat_id),
        text
    )

    return json_response({'detail': 'Response sended'}, status=200)
