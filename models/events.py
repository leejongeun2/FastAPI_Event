from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int  # 자동생성되는 고유 식별자
    title: str  # 이벤트 타이틀
    image: str  # 이벤트 이미지 배너의 링크
    description: str  # 이벤트 설명
    tags: List[str]  # 그룹화를 위한 이벤트 태그
    location: str  # 이벤트 위치

    class Config:  # 샘플 데이터 정의
        schema_extra = {
            "example": {
                "title": "fastapi book launch",
                "image": "https://linktomyimage/image.png",
                "description": "we will be discussing the contents of the fastapi book in this event. ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google meet",
            }
        }
