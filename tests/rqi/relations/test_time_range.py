import datetime as dt

from rqi.intervals import IntervalBoundary
from rqi.relations.time_range import TimeRangeInterval


DEFAULT_INTERVAL_BOUNDARIES = [
    IntervalBoundary.CLOSED_LEFT,
    IntervalBoundary.CLOSED_RIGHT
]

def test_time_range_interval_init():
    # Friday, August 15, 2025 12:00:00 PM
    start_epoch = 1755259200

    # Friday, August 15, 2025 2:00:00 PM
    end_epoch = 1755266400

    tr = TimeRangeInterval(
        start_epoch=start_epoch,
        end_epoch=end_epoch,
        bounds=DEFAULT_INTERVAL_BOUNDARIES
    )
    assert tr.start_epoch == start_epoch
    assert tr.end_epoch == end_epoch
    assert tr.bounds == DEFAULT_INTERVAL_BOUNDARIES
    assert tr.start_dt == dt.datetime(2025, 8, 15, 12, 0, tzinfo=dt.timezone.utc)
    assert tr.end_dt == dt.datetime(2025, 8, 15, 14, 0, tzinfo=dt.timezone.utc)
