from fastapi import Depends, HTTPException, status

# from services.auth_utils import get_current_user
# import database.card_db as card_db


# async def user_with_workspace(user: dict = Depends(get_current_user)):
#     if user['id_workspace'] is None:
#         raise HTTPException(
#             detail='this user dont have workspace',
#             status_code=status.HTTP_400_BAD_REQUEST
#         )

#     return user


# async def card_check_access(id_card: int, user: dict = Depends(user_with_workspace)):
#     id_workspace = user['id_workspace']
#     check_id_workspace = await card_db.get_id_workspace_by_card(id_card)
#     if id_workspace != check_id_workspace:
#         raise HTTPException(
#             detail='user dont have access to this card',
#             status_code=status.HTTP_403_FORBIDDEN
#         )
    
#     return id_card
