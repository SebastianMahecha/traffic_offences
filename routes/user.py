from fastapi import APIRouter, Depends, Query, status, Body
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import List
import httpmodels.user as user_httpmodels
import httpmodels.general as general_httpmodels
import services.user as user_services
import config.db as db
from dataclasses import asdict
import json

router = APIRouter()

@router.get("/users", response_model=user_httpmodels.UserListResponse)
def get_users(
    first_name: str = Query(
        None,
        description="Filter users by first name",
        max_length=255
    ),
    email: str = Query(
        None,
        description="Filter users by email",
        max_length=255
    ),
    session: Session = Depends(db.get_session),
):

    return  user_services.get_users(session, first_name, email)

@router.get(
    "/user/{user_id}", 
    response_model=user_httpmodels.UserResponse,
    responses={
        200: {"description": "User found", "content":  {"application/json": {"example":{"status":"success","message":"","user":{"first_name":"Juan Sebastian","id":1,"last_name":"Mahecha Macias","address":"Ibague","phone":"3108513655","email":"juanmahecha.macias@gmail.com"}}}}},
        400: {"description": "User not found", "content":  {"application/json": {"example":{"status":"error","message":"User not found.","user":None}}}},

    }
)
def get_user(
    user_id: int,
    session: Session = Depends(db.get_session),
):
    response = user_services.get_user_by_id(session, user_id)   
    if not response.user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=asdict(response)
        )
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=asdict(response)
    )


@router.post(
    "/user", 
    response_model = user_httpmodels.UserResponse,
    responses={
        200: {"description": "User found", "content":  {"application/json": {"example":{"status":"success","message":"","user":{"first_name":"Juan Sebastian","id":1,"last_name":"Mahecha Macias","address":"Ibague","phone":"3108513655","email":"juanmahecha.macias@gmail.com"}}}}},
        400: {"description": "User not found", "content":  {"application/json": {"example":{"status":"error","message":"User not found.","user":None}}}},

    }
)
def create_user(
    user_request: user_httpmodels.UserRequest = Body(
        ..., 
        example={
            "first_name": "Juan Sebastian",
            "last_name": "Mahecha Macias",
            "address": "Ibague - Tolima",
            "phone": "3108513655",
            "email": "juanmahecha.macias@gmail.com"
        }
    ),
    session: Session = Depends(db.get_session),
):
    
    response = user_services.create_user(session, user_request)   
    if not response.user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=asdict(response)
        )
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=asdict(response)
    )

@router.put(
    "/user/{user_id}", 
    response_model = user_httpmodels.UserResponse,
    responses={
        200: {"description": "User found", "content":  {"application/json": {"example":{"status":"success","message":"","user":{"first_name":"Juan Sebastian","id":1,"last_name":"Mahecha Macias","address":"Ibague","phone":"3108513655","email":"juanmahecha.macias@gmail.com"}}}}},
        400: {"description": "User not found", "content":  {"application/json": {"example":{"status":"error","message":"User not found.","user":None}}}},
    }
)
def update_user(
    user_id: int,
    user_request: user_httpmodels.UserRequest = Body(
        ..., 
        example={
            "first_name": "Juan Sebastian",
            "last_name": "Mahecha Macias",
            "address": "Ibague - Tolima",
            "phone": "3108513655",
            "email": "juanmahecha.macias@gmail.com"
        }
    ),
    session: Session = Depends(db.get_session),
):
    
    response = user_services.update_user(session, user_id, user_request)   
    if response.status == "error":
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=asdict(response)
        )
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=asdict(response)
    )


@router.delete(
    "/user/{user_id}", 
    response_model=general_httpmodels.GeneralResponse,
    responses={
        200: {"description": "User found", "content":  {"application/json": {"example":{"status":"error","message":"User deleted."}}}},
        400: {"description": "User not found", "content":  {"application/json": {"example":{"status":"error","message":"User not found."}}}},

    }
)

def get_user(
    user_id: int,
    session: Session = Depends(db.get_session),
):
    response = user_services.delete_user_by_id(session, user_id)   
    if response.status == "error":
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content=asdict(response)
        )
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=asdict(response)
    )
