# pylint: disable=too-few-public-methods
"""
Asset Hours DAO. An asset is any entity which has an interval.
"""

from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.postgresql import TSRANGE

from intervals.models import CanonicalDay, Base


class AssetHours(Base):
    """AssetHours DAO."""
    __tablename__ = 'asset_hours'

    id = Column(Integer, primary_key=True)
    day = Column(Enum(CanonicalDay, name="canonical_day"), nullable=False)
    open_interval = Column(TSRANGE, nullable=False)  # e.g., 09:00-17:00
