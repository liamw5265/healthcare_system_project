from app.models.model_base import Base

from sqlalchemy import ForeignKey, String, DATETIME, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Diagnosis_Record(Base):
    __tablename__ = 'diagnosis_records'

    diagnosis_id = mapped_column(
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

    provider_id = mapped_column(
        SMALLINT(unsigned = True),
        ForeignKey('providers.provider_id'),
        nullable = False
    )

    diagnosis_code = mapped_column(
        String(30),
        ForeignKey('diagnosis_codes.diagnosis_code'),
        nullable = False
    )

    created_at = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP')
    )

    encounters = relationship(
        'Encounter',
        back_populates = 'diagnosis_records'
    )

    patients = relationship(
        'Patient',
        back_populates = 'diagnosis_records'
    )

    providers = relationship(
        'Provider',
        back_populates = 'diagnosis_records'
    )

    diagnosis_codes = relationship(
        'Diagnosis_Code',
        back_populates = 'diagnosis_records'
    )
