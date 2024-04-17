from datetime import datetime, timedelta


from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

# from database.admins_db import get_admin_by_email
import params.auth as auth
from params.confing import TEST
import database.user_db as db
from database.models.user_models import Users


def hash_password(password: str) -> str:
    return auth.pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return auth.pwd_context.verify(plain_password, hashed_password)


async def reg_user(login: str, password: str):
    # user = await db.get_user_by_login(login)
    # if user:
    #     raise HTTPException(
    #         detail='login already exist',
    #         status_code=status.HTTP_400_BAD_REQUEST
    #     )
    
    pass_hash = hash_password(password)
    id_user = await db.reg_user(login, pass_hash)

    return id_user


async def auth_user(login: str, password: str) -> Users:
    user = await db.get_user_by_login(login)
    if not user:
        raise HTTPException(
            detail='login dont exist',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    if not verify_password(password, user.password):
        raise HTTPException(
            detail='password is incorrect',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    return user


# async def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=10080)
#     to_encode.update({'exp': expire})
#     encoded_jwt = jwt.encode(
#         to_encode, 
#         auth.SECRET_KEY, 
#         algorithm=auth.ALGORITHM
#     )
#     return encoded_jwt


def my_auth(request: Request):
    # TODO REFACTORY
    if TEST:
        return 1
    id_user = request.headers.get('id_user')
    if id_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="add 'id_user' to headers"
        )
    
    return int(id_user)


async def get_current_user(id_user: int = Depends(my_auth)) -> Users | None:
    # try:
    #     payload = jwt.decode(
    #         token,
    #         auth.SECRET_KEY,
    #         algorithms=[auth.ALGORITHM]
    #     )
    #     username: str = payload.get('sub')  # type: ignore
    #     if username is None:
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail='could not validate credentials'
    #         )

    # except JWTError:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='could not validate credentials'
    #     )

    user = await db.get_user_by_id(id_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='user not found'
        )

    return user


# async def authenticate_admin(
#     admin_email: str, 
#     password: str
# ):
#     admin = await get_admin_by_email(admin_email)
#     if not admin:
#         return False
#     if not verify_password(
#         password, 
#         admin['admin_password']
#     ):
#         return False
#     return admin


# async def get_current_admin(
#     token: str = Depends(auth.oauth2_scheme_admin)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Could not validate credentials'
#     )

#     try:
#         payload = jwt.decode(
#             token, 
#             auth.SECRET_KEY, 
#             algorithms=[auth.ALGORITHM]
#         )
#         username: str = payload.get('sub')
#         if username is None: raise credentials_exception

#     except JWTError:
#         raise credentials_exception
        
#     admin = await get_admin_by_email(username)
#     if admin is None:
#         raise credentials_exception
#     return admin
