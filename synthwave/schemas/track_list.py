from pydantic import BaseModel
from typing import List, Optional
from synthwave.schemas.track_data import Track

class TrackList(BaseModel):
    tracks: List[Track]
    total_time: Optional[int] = None
    total_tracks: Optional[int] = None