from app.models.model_base import Base

from sqlalchemy import String, DATE, ForeignKey, DATETIME, text, func
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import mapped_column, relationship


class Patient(Base):
    __tablename__ = 'patients'

    patient_id = mapped_column(
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
        String(20),
        nullable = False
    )

    phone = mapped_column(
        String(20)
    )

    email = mapped_column(
        String(255)
    )

    home_address = mapped_column(
        String(255),
        nullable = False
    )

    emergency_contact_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('emergency_contact_info.emergency_contact_id'),
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

    emergency_contact_info = relationship(
        'EmergencyContactInfo',
        back_populates = 'patients'
    )

    appointments = relationship(
        'Appointment',
        back_populates = 'patients'
    )

    encounters = relationship(
        'Encounter',
        back_populates = 'patients'
    )

    diagnosis_records = relationship(
        'Diagnosis_Record',
        back_populates = 'patients'
    )

    orders = relationship(
        'Order',
        back_populates = 'patients'
    )

    lab_results = relationship(
        'LabResult',
        back_populates = 'patients'
    )

    billing = relationship(
        'Billing',
        back_populates = 'patients'
    )
