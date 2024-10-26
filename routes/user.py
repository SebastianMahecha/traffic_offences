from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
import httpmodels.user as user_httpmodels
import services.user as user_services
import config.db as db

router = APIRouter()

@router.get("/users/", response_model=user_httpmodels.UserListResponse)
def get_users(session: Session = Depends(db.get_session)):

    return  user_services.get_users(session)
        