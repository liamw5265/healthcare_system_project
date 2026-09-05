from app.database import Base

from sqlalchemy import String, Boolean, ForeignKey
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

    departmant_id = mapped_column(
        SMALLINT(unsigned  =True),
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
        nullable = False
    )

    active = mapped_column(
        Boolean,
        nullable = False
    )

    department = relationship(
        'Department',
        back_populates = 'providers'
    )
    