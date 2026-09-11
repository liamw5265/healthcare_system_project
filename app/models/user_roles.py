from app.models.model_base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import mapped_column, relationship


class UserRole(Base):
    __tablename__ = 'user_roles'

    user_id = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('users.user_id'),
        nullable = False,
        primary_key = True
    )

    role_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('roles.role_id'),
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
