from app.database import Base

from sqlalchemy import String, Integer, DATETIME, DATE, TIME
from sqlalchemy.dialects.mysql import SMALLINT, BIGINT
from sqlalchemy.orm import mapped_column, relationship

from datetime import datetime
from zoneinfo import ZoneInfo

class Appointment(Base):
    __tablename__ = 'appointments'

    appointment = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    parient_id = mapped_column(
        Integer(unsigned = True),
        nullable = False
    )

    provider_id = mapped_column(
        SMALLINT(unsigned = True),
        nullable = True
    )

    department_id = mapped_column(
        SMALLINT(unsigned = False),
        nullable = False
    )

    appointment_date = mapped_column(
        DATE,
        nullable = False
    )

    appointment_time = mapped_column(
        TIME,
        nullable = False
    )

    appointment_type = mapped_column(
        String(100),
        nullable = False
    )

    reason = mapped_column(
        String(500)
    )

    status = mapped_column(
        String(30),
        nullable = False
    )

    check_in_time = mapped_column(
        TIME,
        nullable = False
    )

    created_at = mapped_column(
        DATETIME,
        nullable = False,
        default = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S')
    )

    updated_at = mapped_column(
        DATETIME,
        nullable = False,
        default = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S'),
        onupdate = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S')
    )

    patients = relationship(
        'appointments',
        back_populates = 'patients'
    )

    providers = relationship(
        'appointments',
        back_populates = 'providers'
    )

    departments = relationship(
        'appointments',
        back_populates = 'departments'
    )