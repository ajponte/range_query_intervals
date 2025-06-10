"""
`TimeRangeInterval` class.
Can be used with sqlalchemy's implementation of psql `tsrange`.

Example Usage:

    >> r1 = TimeRangeInterval(1717927200, 1717930800)  # 2024-06-09 10:00–11:00 UTC
    >> r2 = TimeRangeInterval(1717929000, 1717932600)  # 2024-06-09 10:30–11:30 UTC

    >> print(r1.overlaps(r2))  # True
    >> print(r1.contains(1717929000))  # True
    >> print(r1.to_pg_tsrange())
    >> tsrange('2024-06-09 10:00:00', '2024-06-09 11:00:00', '[)')
"""
from datetime import datetime, timezone


class TimeRangeInterval:
    def __init__(self, start_epoch: int, end_epoch: int, bounds: str = '[)'):
        """
        :param start_epoch: start time as UTC epoch int
        :param end_epoch: end time as UTC epoch int
        :param bounds: '[)', '[]', '(]', or '()'
                        `bounds` represent whether the interval is open or closed.
        """
        if start_epoch >= end_epoch:
            raise ValueError("start_epoch must be less than end_epoch")

        if bounds not in ('[)', '[]', '(]', '()'):
            raise ValueError("bounds must be one of '[)', '[]', '(]', '()'")

        self.start_epoch = start_epoch
        self.end_epoch = end_epoch
        self.bounds = bounds

        self._start_dt = datetime.fromtimestamp(start_epoch, tz=timezone.utc)
        self._end_dt = datetime.fromtimestamp(end_epoch, tz=timezone.utc)

    def overlaps(self, other: 'TimeRangeInterval') -> bool:
        """Check if two time ranges overlap."""
        def start_le_end(a_start, a_incl, b_end, b_incl):
            if a_start < b_end:
                return True
            if a_start == b_end:
                return a_incl and b_incl
            return False

        def end_ge_start(a_end, a_incl, b_start, b_incl):
            if a_end > b_start:
                return True
            if a_end == b_start:
                return a_incl and b_incl
            return False

        a_start_incl = self.bounds[0] == '['
        a_end_incl = self.bounds[1] == ']'
        b_start_incl = other.bounds[0] == '['
        b_end_incl = other.bounds[1] == ']'

        return (start_le_end(self.start_epoch, a_start_incl, other.end_epoch, b_end_incl) and
                end_ge_start(self.end_epoch, a_end_incl, other.start_epoch, b_start_incl))

    def contains(self, epoch: int) -> bool:
        """Check if an epoch int is contained in the range."""
        start_cmp = (self.start_epoch <= epoch) if self.bounds[0] == '[' else (self.start_epoch < epoch)
        end_cmp = (epoch <= self.end_epoch) if self.bounds[1] == ']' else (epoch < self.end_epoch)
        return start_cmp and end_cmp

    def to_pg_tsrange(self) -> str:
        """Return PostgreSQL tsrange literal string representation.

        ;return: start, end values as psql tsrange literals.
        """
        start_str = self._start_dt.strftime('%Y-%m-%d %H:%M:%S')
        end_str = self._end_dt.strftime('%Y-%m-%d %H:%M:%S')
        return f"tsrange('{start_str}', '{end_str}', '{self.bounds}')"

    def __repr__(self):
        return f"TimeRange({self.bounds[0]}{self.start_epoch}, {self.end_epoch}{self.bounds[1]})"
