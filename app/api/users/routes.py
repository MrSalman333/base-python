from fastapi import APIRouter, Depends, HTTPException, status

# from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.common_schemas import TokenSchema
from app.api.deps import get_verified_current_user
from app.api.models import User
from app.api.users.schemas import UserRequest, UserResponse
from app.commons.db import Session, get_db
from app.utils import create_access_token, create_refresh_token, get_hashed_password, verify_password

router = APIRouter(prefix="/api/users")


@router.post("/", response_model=UserResponse)
async def create_user(data: UserRequest, session: Session = Depends(get_db)):
    if session.query(User).filter_by(username=data.username).first():
        raise HTTPException(status.HTTP_409_CONFLICT, "Username is already in use")

    if session.query(User).filter_by(username=data.username).first():
        raise HTTPException(status.HTTP_409_CONFLICT, "Username is already in use")

    try:
        user = User(
            username=data.username,
            password=get_hashed_password(data.password),
        )
        session.add(user)
        session.commit()
    except AssertionError as exception_message:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, exception_message.__str__())

    return UserResponse(id=user.id, username=user.username)


@router.post(
    "/login",
    # response_model=TokenSchema
)
def login(
    body: UserRequest,
    session: Session = Depends(get_db),
):
    user: User = (
        session.query(User).filter_by(username=body.username, password=get_hashed_password(body.password)).first()
    )

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return TokenSchema(
        access_token=create_access_token({"id": user.id, "username": user.username, "todos": user.todos}),
        refresh_token=create_refresh_token({"id": user.id, "username": user.username, "todos": user.todos}),
    )


@router.get("/me")
async def read_current_user(
    current_user: UserResponse = Depends(get_verified_current_user),
    session: Session = Depends(get_db),
    # response_model= UserResponse # there is a weird error when using this
):
    user = session.query(User).filter_by(id=current_user["id"]).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return UserResponse(id=user.id, username=user.username)


@router.get("/")
def get_users(session: Session = Depends(get_db)):
    users = session.query(User).limit(10).all()
    response_users = []
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No Users")
    for user in users:
        response_users.append(user.to_response())

    return response_users
