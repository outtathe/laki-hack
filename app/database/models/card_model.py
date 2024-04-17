from sqlalchemy import (
    Column,
    ForeignKey,
    Integer, 
    String,
    Boolean
)
from sqlalchemy.orm import relationship

# from base import Base


# class Products(Base):
#     __tablename__ = 'products'
#     id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     id_workspace = Column(Integer, ForeignKey('workspaces.id'))
#     card = relationship('Cards', backref='products')


# TODO Заготовка для объединения карточек
# Карточка может быть объединена с разными карточками по каждому из маркетов
# class CardGroups(Base):
#     __tablename__ = 'card_groups'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     id_market = Column(Integer, ForeignKey('markets.id'))
#     card = relationship('Cards', backref='card_groups')


# # При удалении карточки надо полностью удалить Cards, CardParams, запись из Products
# class Cards(Base):
#     __tablename__ = 'cards'
#     id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     # TODO возможно надо записать сюда id_category 
#     id_market = Column(Integer, ForeignKey('markets.id'))
#     id_product = Column(Integer, ForeignKey('products.id'))
#     # TODO Подумать на счет организации удаления
#     # is_deleted = Column(Boolean)
#     card_param = relationship('CardParams', backref='cards')


# class CardsOzon(Cards):
#     __tablename__ = 'cards_ozon'
#     # TODO список полей озона


# class CardsWB(Cards):
#     __tablename__ = 'cards_wb'
#     # TODO список полей вайлдбериз


# # TODO подумать на счет общих базовых полей - артикулы, описание и т.д.
# class CardParams(Base):
#     __tablename__ = 'card_params'
#     id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
#     id_card = Column(Integer, ForeignKey('cards.id'))
#     id_category = Column(Integer, ForeignKey('categories.id'))
#     # Нужен ли ForeignKey для параметров и значений?
#     id_param = Column(Integer, ForeignKey('params.id'))
#     id_value = Column(Integer, ForeignKey('values.id'), nullable=True)
#     value = Column(String, default=None, nullable=True)
