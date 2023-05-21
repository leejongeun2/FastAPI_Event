from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])  # 이벤트 라우터 정의

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="event with supplied id does not exist",  # 제공된 ID를 가진 이벤트가 존재하지 않습니다
    )


# 특정 id의 이벤트만 추출하는 라우트에서는 해당 id의 이벤트가 없으면 http예외 404에러발생


# 생성
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message": "event created successfully."}


# id 이벤트 삭제
@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="event with supplied id does not exist",
    )


# 전체삭제
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "event deleted successfully."}
