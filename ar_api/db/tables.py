from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Time
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import Date
from ar_api.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, primary_key=True,
                       index=True)
    name = Column(String, nullable=False)
    coordinates = Column(String, nullable=False)
    job_title = Column(String, default="")

    __table_args__ = (
        UniqueConstraint('name', 'job_title', name="uq_name_job_title"),
    )

