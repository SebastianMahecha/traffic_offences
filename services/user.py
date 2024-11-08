
import httpmodels.user as user_httpmodels
import httpmodels.general as general_httpmodels
import entities.user as user_models
from sqlmodel import select
import config.db as db


def get_users(session, first_name, email):
    
    query = session.query(user_models.User)
    if first_name:
        query = query.filter(user_models.User.first_name.ilike(f"%{first_name}%"))

    if email:
        query = query.filter(user_models.User.email == email)

    users = query.all()

    response = user_httpmodels.UserListResponse(
        status = "success",
        message = "",
        users = users
    )
    return response

def get_user_by_id(session, user_id):
    
    user = session.get(user_models.User, user_id)
    if not user:
        return user_httpmodels.UserResponse(
           status =  "error",
           message = "User not found.",
           user = None
        )
    return  user_httpmodels.UserResponse(
        status = "success",
        message = "",
        user = user
    )

def create_user(session, user_request):
 
    if user_request.email == "":
        return user_httpmodels.UserResponse(
            status = "error",
            message = "Email empty.",
            user = None
        )
    
    user = user_models.User(**user_request.dict())
  
    session.add(user)

    session.commit()
        
    session.refresh(user)
    
    return  user_httpmodels.UserResponse(
        status = "success",
        message = "",
        user = user
    )
  

def update_user(session, user_id, user_request):
    
    user = session.get(user_models.User, user_id)
    
    if not user:
        return user_httpmodels.UserResponse(
                status = "error",
                message = "user not found.",
                user = None
            )
    
    if user_request.email == "":
        return user_httpmodels.UserResponse(
            status = "error",
            message = "Email empty.",
            user = None
        )
  
    user.first_name = user_request.first_name
    user.last_name = user_request.last_name
    user.address = user_request.address
    user.phone = user_request.phone
    user.email = user_request.email

    session.commit()
        
    session.refresh(user)
    
    return  user_httpmodels.UserResponse(
        status = "success",
        message = "",
        user = user
    )
  

def delete_user_by_id(session, user_id):
    
    user = session.get(user_models.User, user_id)
    if not user:
        return general_httpmodels.GeneralResponse(
           status =  "error",
           message = "User not found."
        )
    session.delete(user)
    session.commit()
    return  general_httpmodels.GeneralResponse(
        status = "success",
        message = "User deleted"
    )
