
from dataclasses import dataclass
from pydantic import BaseModel, Field

@dataclass
class GeneralResponse(BaseModel):
    status: str
    message: str
    
    def __init__(self, **data) -> None:
      super().__init__(**data)