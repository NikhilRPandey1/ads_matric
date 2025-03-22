from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.api.accounts.schemas.matrics import AdMetricsFilter, AdMetricsResponse
from app.api.accounts.services.matrics_service import AdMetricsService


router = APIRouter(prefix="/ads", tags=["Matrics"])


@router.get("/matrix/", response_model=List[AdMetricsResponse])
async def get_matrics(
    filters: AdMetricsFilter = Depends(), db: AsyncSession = Depends(get_db)
):
    ad_metrics = await AdMetricsService.get_ad_metrics(db, filters)
    return ad_metrics
