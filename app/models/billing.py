from app.models.model_base import Base

from sqlalchemy import ForeignKey, String, DATETIME, text, func
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, DECIMAL
from sqlalchemy.orm import mapped_column, relationship


class Billing(Base):
    __tablename__ = 'billing'

    billing_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    encounter_id = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('encounters.encounter_id'),
        nullable = False
    )

    patient_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('patients.patient_id'),
        nullable = False
    )

    amount = mapped_column(
        DECIMAL(precision = 10, scale = 2),
        nullable = False
    )

    status = mapped_column(
        String(30),
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

    encounters = relationship(
        'Encounter',
        back_populates = 'billing'
    )

    patients = relationship(
        'Patient',
        back_populates = 'billing'
    )
