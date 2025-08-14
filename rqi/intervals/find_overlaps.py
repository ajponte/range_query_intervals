# pylint: disable=fixme
"""
Driver module for finding open intervals.
"""

from sqlalchemy import select, func

from sqlalchemy.orm import session

from rqi.models.partial_interval import PartialInterval
from rqi.relations.time_range import TimeRangeInterval

def check_time_range(
        start: int,
        end: int,
        time_range: TimeRangeInterval
) -> bool:
    """Returns True only if [start, end] can fit within any bounds of TIME-RANGE."""

    # todo
    return _check_time_range()

def _check_time_range(time_range_one: TimeRangeInterval, time_range_two: TimeRangeInterval):
    """Return True only if the event is within the shop's hours."""
    # todo
    db_session: session = session.Session  # type: ignore
    try:
        query = select(PartialInterval).where(
            func.tsrange(time_range_two.start_dt, time_range_two.end_dt, time_range_two.bounds).op(
                "@>"
            )(PartialInterval.open_interval)
        )
        result = db_session.execute(query).scalars().all()  # type: ignore
        if not result:
            return False
        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False
