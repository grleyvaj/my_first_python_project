from fastapi import APIRouter, HTTPException, Path
from starlette import status

from my_fastapi.v1.schemas.user import UserCreateRequest, UserCreateResponse, UserCreateResponseMapper
from my_fastapi.v1.services.user.user_service import UserService

router = APIRouter()

user_create_response_mapper = UserCreateResponseMapper()
user_service = UserService()


@router.post(path="/api/v1/users", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserCreateRequest) -> UserCreateResponse:
    user = user_service.create(user_request)

    return user_create_response_mapper.mapper(user)


@router.get(
    path="/api/v1/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserCreateResponse,
)
async def get_user(user_id: int = Path(gt=0)) -> UserCreateResponse:
    user = user_service.get_user(user_id)

    if user:
        return user_create_response_mapper.mapper(user)

    raise HTTPException(404, "User not found")


@router.delete(path="/api/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int = Path(gt=0)) -> None:  # noqa: B008
    user = user_service.get_user(user_id)

    if user:
        user_service.delete(user)
    else:
        raise HTTPException(404, "User not found")
