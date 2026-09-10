from model_base import Base

from sqlalchemy import String, DATETIME, DATE, TIME, ForeignKey
from sqlalchemy.dialects.mysql import SMALLINT, INTEGER, BIGINT
from sqlalchemy.orm import mapped_column, relationship

from datetime import datetime, timezone

class Appointment(Base):
    __tablename__ = 'appointments'

    appointment = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    parient_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('patients.parient_id'),
        nullable = False
    )

    provider_id = mapped_column(
        SMALLINT(unsigned = True),
        ForeignKey('providers.provider_id'),
        nullable = True
    )

    department_id = mapped_column(
        SMALLINT(unsigned = False),
        ForeignKey('departments.department_id'),
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
        default = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    )

    updated_at = mapped_column(
        DATETIME,
        nullable = False,
        default = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
        onupdate = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    )

    patients = relationship(
        'Patient',
        back_populates = 'appointments'
    )

    providers = relationship(
        'Provider',
        back_populates = 'appointments'
    )

    departments = relationship(
        'Department',
        back_populates = 'appointments'
    )