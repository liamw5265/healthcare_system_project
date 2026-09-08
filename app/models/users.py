from app.database import Base

from sqlalchemy import String, Boolean, DATETIME
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import mapped_column, relationship

from datetime import datetime
from zoneinfo import ZoneInfo



class User(Base):
    __tablename__ = 'users'

    user_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    username = mapped_column(
        String(100),
        unique = True,
        nullable = False
    )

    password_hash = mapped_column(
        String(255),
        nullable = False
    )

    first_name = mapped_column(
        String(100),
        nullable = False
    )

    last_name = mapped_column(
        String(100),
        nullable = False
    )

    phone = mapped_column(
        String(20),
        unique = True,
        nullable = False
    )

    email = mapped_column(
        String(255),
        unique = True,
        nullable = False
    )

    active = mapped_column(
        Boolean,
        nullable = False,
        default = True
    )

    created_at = mapped_column(
        DATETIME,
        nullable = False,
        default = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S')
    )