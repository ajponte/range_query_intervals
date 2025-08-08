"""Shared DAO module."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum

Base = declarative_base()

# pylint: disable=too-many-ancestors
class CanonicalDay(Enum):
    """Represents a day of the week in human-readable form."""
    SUNDAY = 'SUNDAY'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
