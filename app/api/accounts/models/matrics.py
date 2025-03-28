from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from app.db.base import Base


class FactAdBulletinDaily(Base):
    __tablename__ = "fact_ad_bulletin_daily"

    id = Column(Integer, primary_key=True, index=True)
    date_id = Column(Integer, ForeignKey("dim_date.date_id"))
    region_id = Column(Integer, ForeignKey("dim_region.region_id"))
    age_id = Column(Integer, ForeignKey("dim_age_group.age_id"))
    gender_id = Column(Integer, ForeignKey("dim_gender.gender_id"))
    platform_id = Column(Integer, ForeignKey("dim_platform.platform_id"))
    placement_id = Column(Integer, ForeignKey("dim_placement.placement_id"))
    device_type_id = Column(Integer, ForeignKey("dim_device_type.device_type_id"))
    impressions = Column(Integer)
    clicks = Column(Integer)
    cost = Column(Float)
    conversions = Column(Integer)
    likes = Column(Integer)


class DimDate(Base):
    __tablename__ = "dim_date"
    date_id = Column(Integer, primary_key=True)
    date_value = Column(Date)


class DimRegion(Base):
    __tablename__ = "dim_region"
    region_id = Column(Integer, primary_key=True)
    region_name = Column(String)


class DimAgeGroup(Base):
    __tablename__ = "dim_age_group"
    age_id = Column(Integer, primary_key=True)
    age_range = Column(String)


class DimGender(Base):
    __tablename__ = "dim_gender"
    gender_id = Column(Integer, primary_key=True)
    gender_name = Column(String)


class DimPlatform(Base):
    __tablename__ = "dim_platform"
    platform_id = Column(Integer, primary_key=True)
    platform_name = Column(String)


class DimPlacement(Base):
    __tablename__ = "dim_placement"
    placement_id = Column(Integer, primary_key=True)
    placement_name = Column(String)


class DimDeviceType(Base):
    __tablename__ = "dim_device_type"
    device_type_id = Column(Integer, primary_key=True)
    device_type_name = Column(String)
