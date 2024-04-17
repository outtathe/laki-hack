import aiohttp_cors
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp_cors import setup as cors_setup, ResourceOptions

import src.api as api
import src.config as config
from src.handlers import router


async def on_startup(bot: Bot, base_url: str):
    await bot.delete_webhook()
    await bot.set_webhook(f'{base_url}/webhook')


async def on_shutdown(bot: Bot):
    await bot.delete_webhook()


@web.middleware
async def cors_middleware(request, handler):
    response = await handler(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


async def main():
    bot = Bot(token=config.TOKEN)

    dispatcher = Dispatcher()
    dispatcher['base_url'] = f'https://{config.BOT_URL}/api'
    dispatcher.include_router(router)
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    app = Application()
    app['bot'] = bot
    app['base_url'] = f'https://{config.BOT_URL}/api'
    app.router.add_post('/send_msg', api.send_message)

    cors = aiohttp_cors.setup(app, defaults={
        '*': ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*'
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)

    SimpleRequestHandler(
        dispatcher=dispatcher, 
        bot=bot
    ).register(app, path='/webhook')

    setup_application(app, dispatcher, bot=bot)
    return app
