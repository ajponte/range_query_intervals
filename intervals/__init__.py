"""
Shared module for operating on intervals.
"""

from enum import StrEnum


class IntervalBoundary(StrEnum):
    """Represents interval boundaries"""

    CLOSED_LEFT = "["
    CLOSED_RIGHT = "]"
    OPEN_LEFT = "("
    OPEN_RIGHT = ")"

    @classmethod
    def boundaries(cls):
        """Return all the interval values this enum can point to."""
        return list(cls.__members__.values())

    @classmethod
    def validate(cls, upper: "IntervalBoundary", lower: "IntervalBoundary") -> bool:
        """Validate that boundaries are correct."""
        return all([lower in cls.boundaries() and upper in cls.boundaries()])
