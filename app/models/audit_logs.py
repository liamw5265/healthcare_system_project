from app.models.model_base import Base

from sqlalchemy import ForeignKey, String, DATETIME, text, TEXT
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import mapped_column, relationship


class AuditLog(Base):
    __tablename__ = 'audit_logs'

    audit_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    user_id = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('users.user_id')
    )

    action = mapped_column(
        String(50),
        nullable = False
    )

    table_name = mapped_column(
        String(100)
    )

    record_id = mapped_column(
        BIGINT(unsigned = True)
    )

    action_timestamp = mapped_column(
        DATETIME,
        nullable = False,
        server_default = text('CURRENT_TIMESTAMP')
    )

    ip_address = mapped_column(
        String(45)
    )

    details = mapped_column(
        TEXT
    )

    users = relationship(
        'User',
        back_populates = 'audit_logs'
    )
