from fastapi import APIRouter, HTTPException

from app.auth.token import Token
from app.schemes.auth import RegisterRequest, LoginRequest
from app.services.user_service import UserService

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(request: RegisterRequest):

    user = UserService.register(
        request.full_name,
        request.email,
        request.password,
        request.role,
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )

    return {
        "success": True,
        "message": "User Registered Successfully",
    }


@router.post("/login")
def login(request: LoginRequest):

    user = UserService.login(
        request.email,
        request.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials",
        )

    token = Token.create_access_token(
        {
            "sub": user.email,
            "role": user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role,
        "name": user.full_name,
    }