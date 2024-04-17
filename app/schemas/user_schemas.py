from datetime import datetime

from pydantic import BaseModel, conint


class UserRegistration(BaseModel):
    login: str
    password: str


class UserLoginOut(BaseModel):
    id_user: str
    msg: str


class NewUserData(BaseModel):
    name: str | None
    surname: str | None
    fathername: str | None
    login: str | None
    password: str | None
    telegram: str | None
    tg_id: str | None
    competence_list: list[int] | None


class HackData(BaseModel):
    complexity: conint(ge=1, le=10) | None # От 1 до 10
    organiser: str | None
    detail: str| None
    start_prticipation_date: datetime | None
    end_prticipation_date: datetime | None
    start_registration_date: datetime | None
    end_registration_date: datetime | None
    # team_id: int


class TeamData(BaseModel):
    name: str  | None
    is_national: bool | None


class CompetencesData(BaseModel):
    name: str


class ChatInput(BaseModel):
    model: str
    partial_results: bool
    temperature: float
    max_tokens: int
    role: str
    text: str
    instruction_text: str


class BotCheck(BaseModel):
    tg_name: str
    user_id: int


class BotSendMsg(BaseModel):
    chat_id: int
    text: str


class BotSaveChat(BaseModel):
    chat_id: int
    user_id: int 
