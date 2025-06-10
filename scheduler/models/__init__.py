from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum

Base = declarative_base()

class CanonicalDay(Enum):
    SUNDAY = 'SUNDAY'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
