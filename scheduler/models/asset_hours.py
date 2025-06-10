from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.postgresql import TSRANGE

from scheduler.models import CanonicalDay, Base


class AssetHours(Base):
    __tablename__ = 'store_hours'

    id = Column(Integer, primary_key=True)
    day = Column(Enum(CanonicalDay, name="canonical_day"), nullable=False)
    open_interval = Column(TSRANGE, nullable=False)  # e.g., 09:00-17:00
