from sqlalchemy import select, func
from datetime import datetime

from sqlalchemy.orm import session

from scheduler.models.event import Event
from scheduler.models.asset_hours import AssetHours
from time_range import TimeRangeInterval


def check_hours(
    asset: str,
    time_range: TimeRangeInterval,
    timezone: str = 'UTC'
):
    """Return True only if the event is within the shop's hours.
    """
    try:
        query = select(AssetHours).where(
            func.tsrange(
                time_range._start_dt,
                time_range._end_dt,
                time_range.bounds
            ).op('@>')(AssetHours.open_interval)
        )
        result = session.execute(query).scalars().all()
        print(f'Asset {asset} hours: {result}')
        if not result:
            raise ValueError("Event outside store open hours")
        return True
    except Exception as e:
        print(f'Exception: {e}')
        return False
    finally:
        print("Finally returning False")
        return False


def search_range():
    # Define a range to search for, e.g., June 9, 2025, 10:00 to 11:00
    start_time = datetime(2025, 6, 9, 10, 0)
    end_time = datetime(2025, 6, 9, 11, 0)

    # Build a tsrange using PostgreSQL function `tsrange`
    time_range = func.tsrange(start_time, end_time, '[]')  # inclusive bounds

    # Build the query: find events where time_slot overlaps with the given range
    stmt = select(Event).where(Event.time_slot.op("&&")(time_range))

    # Execute query with a session (assuming session is your SQLAlchemy session)
    results = session.execute(stmt).scalars().all()

    for event in results:
        print(f"Event ID: {event.id}, Day: {event.day}, Time Slot: {event.time_slot}")
