from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.auth_service import AuthService
from app.schemas.refresh_schema import RefreshToken
from app.core.users_service import UsersService
from app.schemas.user_schema import UserCreationDto
from fastapi import Request

class AuthRouter:
    def __init__(self, auth_service: AuthService, users_service: UsersService):
        self.auth_service = auth_service
        self.users_service = users_service
        self.router = APIRouter(tags=["auth"], prefix="/api/v1")

    def get_router(self) -> APIRouter:
        self.router.post("/signin")(self.singin)
        self.router.post("/refresh")(self.refresh)
        self.router.post("/signup")(self.signup)
        #self.router.post('/signingoogle')(self.login_via_google)
        #self.router.post('/auth')(self.auth_via_google)
        return self.router

    async def singin(
        self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> dict:
        user_id, role = await self.auth_service.authenticate_user(
            form_data.username, form_data.password
        )
        access_token = self.auth_service.create_access_token(user_id, role)
        refresh_token = await self.auth_service.create_refresh_token(user_id)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    async def refresh(self, refresh_token: RefreshToken) -> dict:
        user_id, role = await self.auth_service.get_by_refresh_token(
            refresh_token.refresh_token
        )
        return {
            "access_token": self.auth_service.create_access_token(user_id, role),
            "refresh_token": await self.auth_service.create_refresh_token(user_id),
            "token_type": "bearer",
        }

    async def signup(self, user_dto: UserCreationDto) -> dict:
        user_id = await self.users_service.create_user(user_dto.model_dump())
        return {"user_id": user_id}

    async def login_via_google(self, request: Request):
        return await self.auth_service.login_via_google(request)

    async def auth_via_google(self, request: Request):
        return await self.auth_service.auth_via_google(request)
