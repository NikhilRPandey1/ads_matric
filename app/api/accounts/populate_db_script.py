import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from .models.matrics import (
    FactAdBulletinDaily,
    DimDate,
    DimRegion,
    DimAgeGroup,
    DimGender,
    DimPlatform,
    DimPlacement,
    DimDeviceType,
)

fake = Faker()

REGIONS = ["North America", "Europe", "Asia", "South America", "Africa", "Australia"]
AGE_GROUPS = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
GENDERS = ["Male", "Female", "Non-binary"]
PLATFORMS = ["Facebook", "Google Ads", "Instagram", "Twitter", "LinkedIn"]
PLACEMENTS = ["Banner", "Sidebar", "Feed", "Pop-up", "Video"]
DEVICE_TYPES = ["Desktop", "Mobile", "Tablet"]


async def populate_dimension_tables(session: AsyncSession):
    """Populate dimension tables with initial data."""
    dates = []
    start_date = datetime(2023, 1, 1)
    for i in range(365):
        date_obj = DimDate(
            date_id=i + 1,
            date_value=(start_date + timedelta(days=i)).date(),
        )
        dates.append(date_obj)
    session.add_all(dates)

    regions = [
        DimRegion(region_id=i + 1, region_name=name) for i, name in enumerate(REGIONS)
    ]
    session.add_all(regions)

    age_groups = [
        DimAgeGroup(age_id=i + 1, age_range=age) for i, age in enumerate(AGE_GROUPS)
    ]
    session.add_all(age_groups)

    genders = [
        DimGender(gender_id=i + 1, gender_name=gender)
        for i, gender in enumerate(GENDERS)
    ]
    session.add_all(genders)

    platforms = [
        DimPlatform(platform_id=i + 1, platform_name=platform)
        for i, platform in enumerate(PLATFORMS)
    ]
    session.add_all(platforms)

    placements = [
        DimPlacement(placement_id=i + 1, placement_name=placement)
        for i, placement in enumerate(PLACEMENTS)
    ]
    session.add_all(placements)

    device_types = [
        DimDeviceType(device_type_id=i + 1, device_type_name=device)
        for i, device in enumerate(DEVICE_TYPES)
    ]
    session.add_all(device_types)

    await session.commit()
    return {
        "dates": len(dates),
        "regions": len(regions),
        "age_groups": len(age_groups),
        "genders": len(genders),
        "platforms": len(platforms),
        "placements": len(placements),
        "device_types": len(device_types),
    }


async def populate_fact_table(session: AsyncSession, num_entries: int = 1000):
    """Populate fact_ad_bulletin_daily with fake data."""
    fact_entries = []
    for i in range(1, num_entries + 1):
        entry = FactAdBulletinDaily(
            id=i,
            date_id=random.randint(1, 365),
            region_id=random.randint(1, len(REGIONS)),
            age_id=random.randint(1, len(AGE_GROUPS)),
            gender_id=random.randint(1, len(GENDERS)),
            platform_id=random.randint(1, len(PLATFORMS)),
            placement_id=random.randint(1, len(PLACEMENTS)),
            device_type_id=random.randint(1, len(DEVICE_TYPES)),
            impressions=random.randint(100, 10000),
            clicks=random.randint(10, 500),
            cost=round(random.uniform(10.0, 1000.0), 2),
            conversions=random.randint(0, 50),
            likes=random.randint(0, 200),
        )
        fact_entries.append(entry)

    session.add_all(fact_entries)
    await session.commit()
    return num_entries
