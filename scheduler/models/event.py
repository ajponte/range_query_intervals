from sqlalchemy import (
    Column, Integer, Enum, text, Index
)
from sqlalchemy.dialects.postgresql import TSRANGE

from scheduler.models import CanonicalDay


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    time_slot = Column(TSRANGE, nullable=False)
    day = Column(Enum(CanonicalDay, name="canonical_day"), nullable=False)



    __table_args__ = (
        # GiST index for efficient range queries on time_slot
        Index("ix_events_time_slot", "time_slot", postgresql_using="gist"),

        # Exclusion constraint to prevent overlapping time_slot ranges
        text("EXCLUDE USING gist (time_slot WITH &&)"),
    )
