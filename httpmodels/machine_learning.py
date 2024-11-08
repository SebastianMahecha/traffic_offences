
from typing import List
from dataclasses import dataclass
import entities.user as user_models
from typing import Optional
from pydantic import BaseModel, Field

from typing import Optional

@dataclass
class PredictData(BaseModel):
    prediction: float
    lower_bound: float
    upper_bound: float
    
    def __init__(self, **data) -> None:
      super().__init__(**data)

@dataclass
class PredictQuantityTrafficOffences(BaseModel):
    status: str
    message: str
    data: PredictData
    
    def __init__(self, **data) -> None:
      super().__init__(**data)

