# pylint: disable=fixme
"""
Driver module for finding open intervals.
"""

from sqlalchemy import select, func

from sqlalchemy.orm import session

from intervals.models.partial_interval import PartialInterval
from intervals.time_range import TimeRangeInterval


def check_hours(asset: str, time_range: TimeRangeInterval):
    """Return True only if the event is within the shop's hours."""
    # todo
    db_session: session = session.Session
    try:
        query = select(PartialInterval).where(
            func.tsrange(time_range.start_dt, time_range.end_dt, time_range.bounds).op(
                "@>"
            )(PartialInterval.open_interval)
        )
        result = db_session.execute(query).scalars().all()
        print(f"Asset {asset} hours: {result}")
        if not result:
            raise ValueError("Event outside store open hours")
        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False
