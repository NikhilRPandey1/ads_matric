from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.api.accounts.schemas.matrics import AdMetricsFilter, AdMetricsResponse
from app.api.accounts.services.matrics_service import AdMetricsService
from .populate_db_script import populate_dimension_tables, populate_fact_table

router = APIRouter(prefix="/ads", tags=["Matrics"])


@router.get("/matrix/", response_model=List[AdMetricsResponse])
async def get_matrics(
    filters: AdMetricsFilter = Depends(), db: AsyncSession = Depends(get_db)
):
    ad_metrics = await AdMetricsService.get_ad_metrics(db, filters)
    return ad_metrics


@router.post("/populate/")
async def populate_database(
    num_entries: int = 1000, db: AsyncSession = Depends(get_db)
):
    try:
        dim_counts = await populate_dimension_tables(db)

        fact_count = await populate_fact_table(db, num_entries)
        return {
            "message": "Database populated successfully",
            "dimension_tables": dim_counts,
            "fact_table_entries": fact_count,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error populating database: {str(e)}"
        )
