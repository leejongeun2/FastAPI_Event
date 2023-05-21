from fastapi import APIRouter, HTTPException, status
from models.users import User, Usersign


user_router = APIRouter(
    tags=["User"],
)
users = {}


@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:  # 사용자를 등록하기 전 데이터베이스에 비슷한 이메일이 존재하는지 확인
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="users with supplied username exists",  # 제공된 사용자 이름을 가진 사용자가 존재합니다
        )
    users[data.email] = data
    # users 딕셔너리에 사용자의 이메일 주소를 키로 하고, User 객체를 값으로 해서 새로운 항목을 추가
    return {"message": "user successfully registered!"}


@user_router.post("/signin")
async def sign_user_in(user: Usersign) -> dict:
    if user.email not in users:  # 로그인하려는 사용자가 데이터베이스에 존재하는지를 먼저 확인
        raise HTTPException(  # 없으면 예외 발생
            status_code=status.HTTP_404_NOT_FOUND, detail="user does not exist"
        )
    if users[user.email].password != user.password:  # 사용자가 존재하면 패스워드가 일치하는지 확인
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="wrong passed"
        )
    return {"message": "user signed in successfully"}
