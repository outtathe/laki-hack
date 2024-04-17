from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from . import config as config


web_app_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='C L I C K',
            web_app=WebAppInfo(
                url=f'https://{config.BOT_URL}')
        )]
    ]
)
