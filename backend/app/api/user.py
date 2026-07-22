from fastapi import APIRouter, Depends, HTTPException

from app.auth.oauth2 import get_current_user
from app.auth.roles import admin_required
from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/api/user",
    tags=["User"],
)


# ==========================================================
# Current Logged-in User
# ==========================================================

@router.get("/me")
def get_current_profile(current_user=Depends(get_current_user)):
    """
    Returns the currently logged-in user's JWT information.
    """

    return {
        "success": True,
        "user": current_user,
    }


# ==========================================================
# Admin Only - List All Users
# ==========================================================

@router.get("/all")
def get_all_users(current_user=Depends(admin_required)):
    """
    Returns all registered users.
    Accessible only by Admin.
    """

    users = DatabaseService.get_all_users()

    return {
        "success": True,
        "total_users": len(users),
        "users": users,
    }


# ==========================================================
# Current User Role
# ==========================================================

@router.get("/role")
def get_user_role(current_user=Depends(get_current_user)):
    """
    Returns current user's role.
    """

    return {
        "success": True,
        "role": current_user.get("role"),
    }


# ==========================================================
# Dashboard Summary
# ==========================================================

@router.get("/dashboard")
def dashboard_info(current_user=Depends(get_current_user)):
    """
    Returns dashboard information based on logged-in user.
    """

    return {
        "success": True,
        "name": current_user.get("name"),
        "email": current_user.get("sub"),
        "role": current_user.get("role"),
        "message": f"Welcome {current_user.get('name')} to SentinelAI",
    }