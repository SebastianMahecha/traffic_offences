
from typing import List
from dataclasses import dataclass
import entities.user as user_models
from typing import Optional
from pydantic import BaseModel, Field

from typing import Optional

class UserListResponse(BaseModel):
    status: str
    message: str
    users: List[user_models.User]
    
    def __init__(self, status: str, message: str, users: List[user_models.User]):
        self.status = status
        self.message = message
        self.users = users

    def __init__(self, **data) -> None:
      super().__init__(**data)

class UserRequest(BaseModel):
    first_name: str = Field(...,  description="User First Name")  
    last_name: str = Field(..., description="User Last Name")  
    address: Optional[str] =  Field(None, description="User Address")
    phone: Optional[str] = Field(None, description="User Phone")
    email: Optional[str] = Field(None, description="User Email")
    
@dataclass
class UserResponse(BaseModel):
    status: str
    message: str
    user: Optional[user_models.User]
    
    def __init__(self, **data) -> None:
      super().__init__(**data)