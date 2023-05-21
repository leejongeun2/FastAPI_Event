from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr  # 사용자 이메일
    password: str  # 사용자 패스워드
    events: Optional[List[Event]]  # 해당 사용자가 생성한 이벤트. 처음에는 비어있다.

    class Config:
        schema_extra = {
            "example": {
                "email": "tmsnvl95@naver.com",
                "password": "strong!",
                "events": [],
            }
        }


class Usersign(BaseModel):
    email: EmailStr  # 사용자 이메일
    password: str  # 사용자 패스워드

    class Config:
        schema_extra = {
            "example": {
                "email": "tmsnvl95@naver.com",
                "password": "strong!",
                # "evenets": [],
            }
        }
