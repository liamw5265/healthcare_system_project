from app.database import Base

from sqlalchemy import String, Integer, DATE
from sqlalchemy.orm import mapped_column, relationship


class EmergencyContactInfo(Base):
    __tablename__ = 'emergency_contact_info'

    emergency_contact_id = mapped_column(
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

    patients = relationship(
        'emergency_contact_info',
        back_populates = 'patients'
    )