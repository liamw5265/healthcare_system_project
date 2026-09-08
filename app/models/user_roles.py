from app.database import Base

from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import mapped_column, relationship

class UserRole(Base):
    __tablename__ = 'user_roles'

    user_id = mapped_column(
        BIGINT(unsigned = True),
        nullable = False,
        primary_key = True
    )

    role_id = mapped_column(
        Integer(unsigned = True),
        nullable = False,
        primary_key = True
    )

    users = relationship(
        'User',
        back_populates = 'user_roles'
    )

    roles = relationship(
        'Role',
        back_populates = 'user_roles'
    )