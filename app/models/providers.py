from app.models.model_base import Base

from sqlalchemy import String, ForeignKey, Boolean, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Provider(Base):
    __tablename__ = 'providers'

    provider_id = mapped_column(
        SMALLINT(unsigned = True),
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

    department_id = mapped_column(
        SMALLINT(unsigned = True),
        ForeignKey('departments.department_id'),
        nullable = False
    )

    specialty = mapped_column(
        String(100)
    )

    phone = mapped_column(
        String(20),
        nullable = False
    )

    email = mapped_column(
        String(255),
        nullable = False,
        unique = True
    )

    active = mapped_column(
        Boolean,
        nullable = False,
        default = True,
        server_default = text('TRUE')
    )

    department = relationship(
        'Department',
        back_populates = 'providers'
    )

    appointments = relationship(
        'Appointment',
        back_populates = 'providers'
    )

    encounters = relationship(
        'Encounter',
        back_populates = 'providers'
    )

    diagnosis_records = relationship(
        'Diagnosis_Record',
        back_populates = 'providers'
    )

    orders = relationship(
        'Order',
        back_populates = 'providers'
    )
