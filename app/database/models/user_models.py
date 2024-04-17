from sqlalchemy import (
    Column,
    ForeignKey,
    Integer, 
    String,
    Boolean,
    TIMESTAMP
)
from sqlalchemy.orm import relationship, backref

from .base import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    surname = Column(String)
    fathername = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    telegram = Column(String, unique=True)
    tg_id = Column(Integer, unique=True)
    id_competence_group = Column(Integer, ForeignKey('competence_groups.id', ondelete='CASCADE', onupdate='CASCADE'), default=None, nullable=True)
    competence_groups = relationship('CompetenceGroups', backref='users', lazy='selectin', cascade = "all,delete")
    # competences = relationship('Competences', secondary='competence_groups', backref='users')
    # user_teams = relationship('UserTeams', back_populates = 'users')
    teams = relationship('UserTeams', back_populates='user', lazy='selectin', cascade = "all,delete")


class CompetenceGroups(Base):
    __tablename__ = 'competence_groups'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    # competences = relationship('GroupsOfCompetences', backref='competence_groups')
    competences = relationship('Competences', secondary='groups_of_competences', back_populates='competence_groups', lazy='selectin', cascade = "all,delete")
    # competence_groups = relationship('Users', backref='competence_groups')
    


class GroupsOfCompetences(Base):
    __tablename__ = 'groups_of_competences'
    # id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_group = Column(Integer, ForeignKey('competence_groups.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    id_competence = Column(Integer, ForeignKey('competences.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    # competences = relationship('Competences', backref=backref('competence_groups', lazy='noload'), uselist=True)
    # relationship('Competences', secondary='competence_groups', backref='users')
    # competence_group = relationship('CompetenceGroups', back_populates='competence')
    # competence = relationship('Competences', backref='competence_group')
    
    # __table_args__ = (
    #     UniqueConstraint('id_group', 'id_competence', name='unic_group_competence'),
    # )


class Competences(Base):
    __tablename__ = 'competences'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    # competence_groups = relationship('GroupsOfCompetences', backref='competences')
    competence_groups = relationship('CompetenceGroups', secondary='groups_of_competences', back_populates='competences', cascade = "all,delete")


class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_national = Column(Boolean)
    users = relationship('UserTeams', back_populates='team', uselist=True, lazy='selectin', cascade = "all,delete")


class UserTeams(Base):
    __tablename__ = 'user_teams'
    id_team = Column(Integer, ForeignKey('teams.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    id_competence_group = Column(Integer, ForeignKey('competence_groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    competence_groups = relationship('CompetenceGroups', backref='user_teams', cascade = "all,delete")
    user = relationship('Users', back_populates='teams', uselist=True, cascade = "all,delete")
    team = relationship('Teams', back_populates='users', uselist=True, cascade = "all,delete")


class Hackathon(Base):
    __tablename__ = 'hackathon'
    id = Column(Integer, primary_key=True)
    complexity = Column(Integer) # От 1 до 10
    organiser = Column(String)
    detail = Column(String)
    start_prticipation_date = Column(type_=TIMESTAMP(timezone=True))
    end_prticipation_date = Column(type_=TIMESTAMP(timezone=True))
    start_registration_date = Column(type_=TIMESTAMP(timezone=True))
    end_registration_date = Column(type_=TIMESTAMP(timezone=True))
    id_team = Column(Integer, ForeignKey('teams.id', ondelete='CASCADE', onupdate='CASCADE'))
    teams = relationship('Teams', backref='hackathons', uselist=True, lazy='selectin', cascade = "all,delete")
