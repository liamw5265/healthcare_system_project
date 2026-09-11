from app.models.model_base import Base

from sqlalchemy import String, Boolean, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import mapped_column, relationship


class Department(Base):
    __tablename__ = 'departments'

    department_id = mapped_column(
        SMALLINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    department_name = mapped_column(
        String(100),
        nullable = False
    )

    department_location = mapped_column(
        String(100),
        nullable = False
    )

    active = mapped_column(
        Boolean,
        nullable = False,
        default = True,
        server_default = text('TRUE')
    )

    providers = relationship(
        'Provider',
        back_populates = 'department'
    )

    appointments = relationship(
        'Appointment',
        back_populates = 'departments'
    )
