from app.models.model_base import Base

from sqlalchemy import String, TEXT
from sqlalchemy.orm import mapped_column, relationship


class Diagnosis_Code(Base):
    __tablename__ = 'diagnosis_codes'

    diagnosis_code = mapped_column(
        String(30),
        nullable = False,
        primary_key = True
    )

    diagnosis_name = mapped_column(
        String(255),
        nullable = False
    )

    diagnosis_text = mapped_column(
        TEXT
    )

    diagnosis_records = relationship(
        'Diagnosis_Record',
        back_populates = 'diagnosis_codes'
    )
