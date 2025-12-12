from pydantic import BaseModel
from typing import Optional

class Track(BaseModel):
    start: Optional[int] = None
    end: Optional[int] = None
    title: str