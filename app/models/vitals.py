from app.models.model_base import Base

from sqlalchemy import ForeignKey, DATETIME, text
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Vital(Base):
    __tablename__ = 'vitals'

    vital_id = mapped_column(
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

    temperature = mapped_column(
        DECIMAL(precision = 5, scale = 2),
        nullable = False
    )

    heart_rate = mapped_column(
        SMALLINT(unsigned = True),
        nullable = False
    )

    blood_pressure_systolic = mapped_column(
        SMALLINT(unsigned = True),
        nullable = False
    )

    blood_pressure_diastolic = mapped_column(
        SMALLINT(unsigned = True),
        nullable = False
    )

    weight_lb = mapped_column(
        DECIMAL(precision = 6, scale = 2, unsigned = True),
        nullable = False
    )

    height_ft = mapped_column(
        SMALLINT(unsigned = True),
        nullable = False
    )

    height_in = mapped_column(
        DECIMAL(precision = 6, scale = 2, unsigned = True),
        nullable = False
    )

    recorded_by = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('users.user_id'),
        nullable = False
    )

    recorded_at = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP')
    )

    encounters = relationship(
        'Encounter',
        back_populates = 'vitals'
    )

    users = relationship(
        'User',
        back_populates = 'vitals'
    )
