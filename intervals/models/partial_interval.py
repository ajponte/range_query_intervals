# pylint: disable=too-few-public-methods
"""
Asset Hours DAO. An asset is any entity which has an interval.
"""

from sqlalchemy import Column, VARCHAR, String
from sqlalchemy.dialects.postgresql import TSRANGE
from sqlalchemy.orm.session import Session

from intervals.models import Base


class PartialInterval(Base):
    """
    Interval DAO.
    Interval of a partially-ordered set P = {p1, p2,...,p}
    """

    __tablename__ = "partial_interval"

    # We search by `open_interval` in tsrange, so the ID here is for
    # surrogate purposes.
    id = Column(String, primary_key=True)

    # Keep a small amount of information about the interval.
    # As the size of this column increases, the longer r/w
    # queries take.
    # In a production-scale system, this would be a foreign key
    # relationship, effectively forming a cartesian product
    # between (`label`, `open_interval`).
    label = Column(VARCHAR(16))

    # Any range of values which converges to a partially-ordered set,
    # given a relation whose output is `label`.
    #
    #
    # In order for these values to convert to a partially-ordered set,
    # they must fill as much of the domain as possible. Note that the
    # range of the relation does not necessarily need to be covered.
    #
    # For example,
    #   [1, 2, 4, 9] might be a partially ordered set with a relation
    #       R(X) -> y, where X = [x1, x2, ..., xn] and
    #       X = the start time of a schedule (in utd), whose selection
    #       was chosen based on a variety of tuned inputs.
    #
    open_interval = Column(TSRANGE, nullable=False)

    @classmethod
    def insert(cls, start: int, label: dict, session: Session) -> str | None:
        """
        Insert a new partial interval record.

        :param label:
        :param start:
        :param session: SqlAlchemy Session object.
        :return: The id of new record.
        """
        new_record_id = None
        try:
            new_range = PartialInterval(open_interval=start, label=label)
            session.add(new_range)
            session.refresh(new_range)
            new_record_id: str = new_range.id
            session.commit()
            return new_record_id
        except Exception as e:
            session.rollback()
            print(f"rolled-back due to error: {e}")
        finally:
            session.close()

        return new_record_id
