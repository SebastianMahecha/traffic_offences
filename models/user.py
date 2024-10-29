
from sqlmodel import SQLModel, Field
from dataclasses import dataclass
from typing import Optional

# Define your SQLModel
@dataclass
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str = Field(default="")  
    last_name: str = Field(default="")  
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
