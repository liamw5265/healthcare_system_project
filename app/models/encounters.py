from app.models.model_base import Base

from sqlalchemy import ForeignKey, DATETIME, String, TEXT, text, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Encounter(Base):
    __tablename__ = 'encounters'

    encounter_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    appointment_id = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('appointments.appointment_id'),
        nullable = False
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

    start_time = mapped_column(
        DATETIME,
        nullable = False
    )

    end_time = mapped_column(
        DATETIME
    )

    status = mapped_column(
        String(30),
        nullable = False
    )

    reason = mapped_column(
        String(500)
    )

    clinical_notes = mapped_column(
        TEXT
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

    appointments = relationship(
        'Appointment',
        back_populates = 'encounters'
    )

    patients = relationship(
        'Patient',
        back_populates = 'encounters'
    )

    providers = relationship(
        'Provider',
        back_populates = 'encounters'
    )

    vitals = relationship(
        'Vital',
        back_populates = 'encounters'
    )

    diagnosis_records = relationship(
        'Diagnosis_Record',
        back_populates = 'encounters'
    )

    orders = relationship(
        'Order',
        back_populates = 'encounters'
    )

    billing = relationship(
        'Billing',
        back_populates = 'encounters'
    )
