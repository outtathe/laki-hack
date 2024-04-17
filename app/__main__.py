# from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi_pagination import add_pagination

from routers import user_router, bot_router
from database.db import db_create


app: FastAPI = FastAPI()

@app.on_event('startup')
async def startup():
    db_create()

origins = [
    'http://localhost', 
    'http://localhost:8080', 
    'http://localhost:3000', 
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# add_pagination(app)

app.include_router(
    user_router,
    prefix='/api',
    tags=['user']
)

app.include_router(
    bot_router,
    prefix='/bot',
    tags=['bot']
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
