from fastapi import APIRouter, HTTPException

from app.auth.token import Token
from app.services.user_service import UserService

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register():

    user = UserService.register(
        full_name="Admin User",
        email="admin@sentinelai.com",
        password="admin123",
        role="Admin",
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
def login():

    user = UserService.login(
        "admin@sentinelai.com",
        "admin123",
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
    }