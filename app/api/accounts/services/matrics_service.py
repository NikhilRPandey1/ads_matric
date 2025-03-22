from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.accounts.models.matrics import (
    DimAgeGroup,
    DimGender,
    DimRegion,
    FactAdBulletinDaily,
    DimDate,
    DimPlatform,
)


class AdMetricsService:
    @staticmethod
    async def get_ad_metrics(db: AsyncSession, filters):
        query = (
            select(FactAdBulletinDaily)
            .join(DimDate, FactAdBulletinDaily.date_id == DimDate.date_id)
            .join(
                DimRegion,
                FactAdBulletinDaily.region_id == DimRegion.region_id,
                isouter=True,
            )
            .join(
                DimAgeGroup,
                FactAdBulletinDaily.age_id == DimAgeGroup.age_id,
                isouter=True,
            )
            .join(
                DimGender,
                FactAdBulletinDaily.gender_id == DimGender.gender_id,
                isouter=True,
            )
            .join(
                DimPlatform,
                FactAdBulletinDaily.platform_id == DimPlatform.platform_id,
                isouter=True,
            )
        )

        # Apply filters dynamically
        if filters.start_date:
            query = query.filter(DimDate.date_value >= filters.start_date)
        if filters.end_date:
            query = query.filter(DimDate.date_value <= filters.end_date)
        if filters.region_id:
            query = query.filter(FactAdBulletinDaily.region_id == filters.region_id)
        if filters.platform_id:
            query = query.filter(FactAdBulletinDaily.platform_id == filters.platform_id)
        if filters.age_id:
            query = query.filter(FactAdBulletinDaily.age_id == filters.age_id)
        if filters.gender_id:
            query = query.filter(FactAdBulletinDaily.gender_id == filters.gender_id)

        # Execute the query asynchronously
        result = await db.execute(query)
        ad_metrics = result.scalars().all()
        return ad_metrics
