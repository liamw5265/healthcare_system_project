from app.models.model_base import Base

from sqlalchemy import ForeignKey, TEXT, String, DATETIME
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import mapped_column, relationship


class LabResult(Base):
    __tablename__ = 'lab_results'

    result_id = mapped_column(
        BIGINT(unsigned = True),
        autoincrement = True,
        nullable = False,
        primary_key = True
    )

    order_id = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('orders.order_id'),
        nullable = False
    )

    patient_id = mapped_column(
        INTEGER(unsigned = True),
        ForeignKey('patients.patient_id'),
        nullable = False
    )

    result_text = mapped_column(
        TEXT
    )

    result_value = mapped_column(
        String(100)
    )

    result_status = mapped_column(
        String(30),
        nullable = False
    )

    completed_at = mapped_column(
        DATETIME
    )

    reviewed_by = mapped_column(
        BIGINT(unsigned = True),
        ForeignKey('users.user_id')
    )

    reviewed_at = mapped_column(
        DATETIME
    )

    orders = relationship(
        'Order',
        back_populates = 'lab_results'
    )

    patients = relationship(
        'Patient',
        back_populates = 'lab_results'
    )

    users = relationship(
        'User',
        back_populates = 'lab_results'
    )
