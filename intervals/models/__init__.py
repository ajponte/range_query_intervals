"""Shared DAO module."""

import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum

Base = declarative_base()


def generate_uuid_hex() -> str:
    """
    Generate a random uuid in hex format.

    :return: A uuid-4 hex.
    """
    return uuid.uuid4().hex


# pylint: disable=too-many-ancestors
class CanonicalDay(Enum):
    """Represents a day of the week in human-readable form."""

    SUNDAY = "SUNDAY"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
