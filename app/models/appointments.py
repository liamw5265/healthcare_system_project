from app.models.model_base import Base

from sqlalchemy import ForeignKey, DATE, TIME, String, DATETIME, text, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Appointment(Base):
    __tablename__ = 'appointments'

    appointment_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    patient_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('patients.patient_id'),
        nullable = False
    )

    provider_id = mapped_column(
        SMALLINT(unsigned = True),
        ForeignKey('providers.provider_id'),
        nullable = False
    )

    department_id = mapped_column(
        SMALLINT(unsigned = True),
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
        server_default = text('CURRENT_TIMESTAMP')
    )

    updated_at = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
        onupdate = func.current_timestamp()
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

    encounters = relationship(
        'Encounter',
        back_populates = 'appointments'
    )
