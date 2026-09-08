from app.database import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship


class Role(Base):
    __tablename__ = 'roles'

    role_id = mapped_column(
        Integer(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    role_name = mapped_column(
        String(100),
        nullable = False
    )

    description = mapped_column(
        String(255)
    )