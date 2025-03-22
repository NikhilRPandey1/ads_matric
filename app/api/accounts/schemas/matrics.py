from pydantic import BaseModel
from typing import Optional
from datetime import date


class AdMetricsFilter(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    region_id: Optional[int] = None
    platform_id: Optional[int] = None
    age_id: Optional[int] = None
    gender_id: Optional[int] = None


class AdMetricsResponse(BaseModel):
    date_id: int
    region_id: int
    age_id: int
    gender_id: int
    platform_id: int
    placement_id: int
    device_type_id: int
    impressions: int
    clicks: int
    cost: float
    conversions: int
    likes: int

    class Config:
        orm_mode = True
