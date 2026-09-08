from app.database import Base

from sqlalchemy import String, Integer, DATETIME, DATE
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import mapped_column, relationship

from datetime import datetime
from zoneinfo import ZoneInfo

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = mapped_column(
        Integer(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    first_name = mapped_column(
        String(100),
        nullable = False
    )

    last_name = mapped_column(
        String(100),
        nullable = False
    )

    date_of_birth = mapped_column(
            DATE,
            nullable = False
        )
    
    sex = mapped_column(
        String(20)
    )

    phone = mapped_column(
        String(20),
        nullable = False
    )

    email = mapped_column(
        String(225)
    )

    home_address = mapped_column(
        String(255)
    )

    emergency_contact_id = mapped_column(
        Integer(unsigned = True),
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

    emergency_contact_info = relationship(
        'patients',
        back_populates = 'emergency_contact_info'
    )

