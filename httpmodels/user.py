

from sqlmodel import SQLModel
from typing import List
import models.user as user_models

class UserListResponse(SQLModel, table=False):
    status: str
    message: str
    users: List[user_models.User]

    def __init__(self, status: str, message: str, users: List[user_models.User]):
        self.status = status
        self.message = message
        self.users = users
