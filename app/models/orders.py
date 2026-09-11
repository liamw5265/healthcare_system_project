from app.models.model_base import Base

from sqlalchemy import ForeignKey, String, DATETIME, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Order(Base):
    __tablename__ = 'orders'

    order_id = mapped_column(
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

    order_type = mapped_column(
        String(30),
        nullable = False
    )

    order_name = mapped_column(
        String(100),
        nullable = False
    )

    status = mapped_column(
        String(30),
        nullable = False
    )

    ordered_at = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP')
    )

    completed_at = mapped_column(
        DATETIME
    )

    encounters = relationship(
        'Encounter',
        back_populates = 'orders'
    )

    patients = relationship(
        'Patient',
        back_populates = 'orders'
    )

    providers = relationship(
        'Provider',
        back_populates = 'orders'
    )

    lab_results = relationship(
        'LabResult',
        back_populates = 'orders'
    )
