from app.models.model_base import Base

from sqlalchemy import String, DATE
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import mapped_column, relationship


class EmergencyContactInfo(Base):
    __tablename__ = 'emergency_contact_info'

    emergency_contact_id = mapped_column(
        INTEGER(unsigned = True),
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
        String(255)
    )

    home_address = mapped_column(
        String(255)
    )

    patients = relationship(
        'Patient',
        back_populates = 'emergency_contact_info'
    )
