from app.database import Base

from sqlalchemy import String, Boolean
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import mapped_column, relationship



class Department(Base):
    __tablename__ = 'departments'

    department_id = mapped_column(
        SMALLINT(unsigned = True),
        primary_key = True,
        autoincrement = True
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
        nullable = False
    )

    providers = relationship(
        'Provider',
        back_populates = 'department'
    )