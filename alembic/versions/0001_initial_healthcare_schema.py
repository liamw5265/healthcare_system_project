"""Create the initial healthcare schema.

Revision ID: 0001_initial_healthcare_schema
Revises:
Create Date: 2026-09-18
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0001_initial_healthcare_schema"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tables represented by the initial SQLAlchemy models."""
    op.execute(
        """
        CREATE TABLE departments (
            department_id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL,
            department_location VARCHAR(100) NOT NULL,
            active BOOLEAN NOT NULL DEFAULT TRUE
        )
        """
    )
    op.execute(
        """
        CREATE TABLE users (
            user_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            active BOOLEAN NOT NULL DEFAULT TRUE,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    op.execute(
        """
        CREATE TABLE roles (
            role_id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            role_name VARCHAR(100) UNIQUE NOT NULL,
            description VARCHAR(255)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE emergency_contact_info (
            emergency_contact_id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            date_of_birth DATE NOT NULL,
            sex VARCHAR(20),
            phone VARCHAR(20) NOT NULL,
            email VARCHAR(255),
            home_address VARCHAR(255)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE diagnosis_codes (
            diagnosis_code VARCHAR(30) NOT NULL PRIMARY KEY,
            diagnosis_name VARCHAR(255) NOT NULL,
            diagnosis_text TEXT
        )
        """
    )
    op.execute(
        """
        CREATE TABLE providers (
            provider_id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            department_id SMALLINT UNSIGNED NOT NULL,
            specialty VARCHAR(100),
            phone VARCHAR(20) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            active BOOLEAN NOT NULL DEFAULT TRUE,
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE patients (
            patient_id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            date_of_birth DATE NOT NULL,
            sex VARCHAR(20) NOT NULL,
            phone VARCHAR(20),
            email VARCHAR(255),
            home_address VARCHAR(255) NOT NULL,
            emergency_contact_id INT UNSIGNED NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (emergency_contact_id) REFERENCES emergency_contact_info(emergency_contact_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE user_roles (
            user_id BIGINT UNSIGNED NOT NULL,
            role_id INT UNSIGNED NOT NULL,
            PRIMARY KEY (user_id, role_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (role_id) REFERENCES roles(role_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE appointments (
            appointment_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            patient_id INT UNSIGNED NOT NULL,
            provider_id SMALLINT UNSIGNED NOT NULL,
            department_id SMALLINT UNSIGNED NOT NULL,
            appointment_date DATE NOT NULL,
            appointment_time TIME NOT NULL,
            appointment_type VARCHAR(100) NOT NULL,
            reason VARCHAR(500),
            status VARCHAR(30) NOT NULL,
            check_in_time TIME NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id),
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE encounters (
            encounter_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            appointment_id BIGINT UNSIGNED NOT NULL,
            patient_id INT UNSIGNED NOT NULL,
            provider_id SMALLINT UNSIGNED NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME,
            status VARCHAR(30) NOT NULL,
            reason VARCHAR(500),
            clinical_notes TEXT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE vitals (
            vital_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            encounter_id BIGINT UNSIGNED NOT NULL,
            temperature DECIMAL(5,2) NOT NULL,
            heart_rate SMALLINT UNSIGNED NOT NULL,
            blood_pressure_systolic SMALLINT UNSIGNED NOT NULL,
            blood_pressure_diastolic SMALLINT UNSIGNED NOT NULL,
            weight_lb DECIMAL(6,2) UNSIGNED NOT NULL,
            height_ft SMALLINT UNSIGNED NOT NULL,
            height_in DECIMAL(6,2) UNSIGNED NOT NULL,
            recorded_by BIGINT UNSIGNED NOT NULL,
            recorded_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id),
            FOREIGN KEY (recorded_by) REFERENCES users(user_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE diagnosis_records (
            diagnosis_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            encounter_id BIGINT UNSIGNED NOT NULL,
            patient_id INT UNSIGNED NOT NULL,
            provider_id SMALLINT UNSIGNED NOT NULL,
            diagnosis_code VARCHAR(30) NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id),
            FOREIGN KEY (diagnosis_code) REFERENCES diagnosis_codes(diagnosis_code)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE orders (
            order_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            encounter_id BIGINT UNSIGNED NOT NULL,
            patient_id INT UNSIGNED NOT NULL,
            provider_id SMALLINT UNSIGNED NOT NULL,
            order_type VARCHAR(30) NOT NULL,
            order_name VARCHAR(100) NOT NULL,
            status VARCHAR(30) NOT NULL,
            ordered_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            completed_at DATETIME,
            FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE lab_results (
            result_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            order_id BIGINT UNSIGNED NOT NULL,
            patient_id INT UNSIGNED NOT NULL,
            result_text TEXT,
            result_value VARCHAR(100),
            result_status VARCHAR(30) NOT NULL,
            completed_at DATETIME,
            reviewed_by BIGINT UNSIGNED,
            reviewed_at DATETIME,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (reviewed_by) REFERENCES users(user_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE billing (
            billing_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            encounter_id BIGINT UNSIGNED NOT NULL,
            patient_id INT UNSIGNED NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            status VARCHAR(30) NOT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (encounter_id) REFERENCES encounters(encounter_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE audit_logs (
            audit_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
            user_id BIGINT UNSIGNED,
            action VARCHAR(50) NOT NULL,
            table_name VARCHAR(100),
            record_id BIGINT UNSIGNED,
            action_timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            ip_address VARCHAR(45),
            details TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """
    )


def downgrade() -> None:
    """Remove the initial healthcare schema in dependency-safe order."""
    for table_name in (
        "audit_logs", "billing", "lab_results", "orders", "diagnosis_records",
        "vitals", "encounters", "appointments", "user_roles", "patients",
        "providers", "diagnosis_codes", "emergency_contact_info", "roles",
        "users", "departments",
    ):
        op.drop_table(table_name)
