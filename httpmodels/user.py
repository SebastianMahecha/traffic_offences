

from sqlmodel import SQLModel, Field
from typing import List
from dataclasses import dataclass
import models.user as user_models
from typing import Optional
from pydantic import BaseModel

from typing import Optional

class UserListResponse(SQLModel, table=False):
    status: str
    message: str
    users: List[user_models.User]

    def __init__(self, status: str, message: str, users: List[user_models.User]):
        self.status = status
        self.message = message
        self.users = users

class UserRequest(BaseModel):
    first_name: str = Field(default="",  description="User First Name")  
    last_name: str = Field( default="", description="User Last Name")  
    address: Optional[str] =  Field(default=None, description="User Address")
    phone: Optional[str] = Field(default=None, description="User Phone")
    email: Optional[str] = Field(default=None, description="User Email")
    
@dataclass
class UserResponse(SQLModel, table=False):
    status: str
    message: str
    user: Optional[user_models.User]