"""Test driver script."""

from rqi.intervals import find_overlaps
from rqi.intervals.find_overlaps import check_time_range
from rqi.relations.time_range import TimeRangeInterval


def test_find_overlaps():
    #  Wednesday, August 13, 2025 9:00:00 PM GMT-07:00
    start = 1755144000
    # Thursday, August 14, 2025 1:00:00 AM GMT-07:00
    end = 1755158400

    # Default bounds to `[]`
    interval = TimeRangeInterval(start_epoch=start, end_epoch=end)


    # Base case
    assert check_time_range(start, end, interval) is True

def main():
    test_find_overlaps()


if __name__ == '__main__':
    main()
