from app.database import Base

from sqlalchemy import String, Integer, DATETIME, DATE, TIME, TEXT
from sqlalchemy.dialects.mysql import SMALLINT, BIGINT
from sqlalchemy.orm import mapped_column, relationship

from datetime import datetime
from zoneinfo import ZoneInfo

class Encounter(Base):
    __tablename__ = 'encounters'

    encoutner_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    appointment_id = mapped_column(
        BIGINT(unsigned = True),
        nullable = False
    )

    patient_id = mapped_column(
        Integer(unsigned = True),
        nullable = False
    )

    provider_id = mapped_column(
        SMALLINT(unsigned = False),
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
        DATETIME,
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
        default = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S')
    )

    updated_at = mapped_column(
        DATETIME,
        nullable = False,
        default = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S'),
        onupdate = datetime.now(ZoneInfo('US/Hawaii')).strftime('%Y-%m-%d %H:%M:%S')
    )

    appointments = relationship(
        'encounters',
        back_populates = 'appointments'
    )

    patients = relationship(
        'encounters',
        back_populates = 'patients'
    )

    providers = relationship(
        'encounters',
        back_populates = 'providers'
    )