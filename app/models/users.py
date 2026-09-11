from app.models.model_base import Base

from sqlalchemy import String, Boolean, text, DATETIME
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import mapped_column, relationship


class User(Base):
    __tablename__ = 'users'

    user_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    username = mapped_column(
        String(100),
        nullable = False,
        unique = True
    )

    password_hash = mapped_column(
        String(255),
        nullable = False
    )

    first_name = mapped_column(
        String(100),
        nullable = False
    )

    last_name = mapped_column(
        String(100),
        nullable = False
    )

    phone = mapped_column(
        String(20),
        nullable = False,
        unique = True
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

    created_at = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP')
    )

    user_roles = relationship(
        'UserRole',
        back_populates = 'users'
    )

    vitals = relationship(
        'Vital',
        back_populates = 'users'
    )

    lab_results = relationship(
        'LabResult',
        back_populates = 'users'
    )

    audit_logs = relationship(
        'AuditLog',
        back_populates = 'users'
    )
