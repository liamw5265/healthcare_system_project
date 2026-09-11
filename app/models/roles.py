from app.models.model_base import Base

from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import mapped_column, relationship


class Role(Base):
    __tablename__ = 'roles'

    role_id = mapped_column(
        INTEGER(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    role_name = mapped_column(
        String(100),
        nullable = False,
        unique = True
    )

    description = mapped_column(
        String(255)
    )

    user_roles = relationship(
        'UserRole',
        back_populates = 'roles'
    )
