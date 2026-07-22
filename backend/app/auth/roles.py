from fastapi import Depends, HTTPException

from app.auth.oauth2 import get_current_user


def admin_required(current_user=Depends(get_current_user)):

    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return current_user


def safety_required(current_user=Depends(get_current_user)):

    if current_user["role"] not in ["Admin", "Safety Officer"]:
        raise HTTPException(
            status_code=403,
            detail="Safety Officer access required",
        )

    return current_user


def operator_required(current_user=Depends(get_current_user)):

    return current_user