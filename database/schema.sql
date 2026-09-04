CREATE DATABASE IF NOT EXISTS healthcare_system_db;

USE healthcare_system_db

CREATE TABLE IF NOT EXISTS patients
(
    patient_id VARCHAR(9) NOT NULL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    sex VARCHAR(10) NOT NULL,
    phone VARCHAR(12) NOT NULL,
    email VARCHAR(50) NOT NULL,
    home_address VARCHAR(255) NOT NULL,
    emergency_contact_id VARCHAR(9) NOT NULL,
    created_on DATE NOT NULL,
    updated_on DATE NOT NULL,

    FOREIGN KEY (emergency_contact_id) REFERENCES emergency_contact_info(emergency_contact_id)


);

CREATE TABLE IF NOT EXISTS providers
(

);

CREATE TABLE IF NOT EXISTS departments
(

);

CREATE TABLE IF NOT EXISTS encounters
(

);

CREATE TABLE IF NOT EXISTS vitals
(

);

CREATE TABLE IF NOT EXISTS diagnoses
(

);

CREATE TABLE IF NOT EXISTS orders
(

);

CREATE TABLE IF NOT EXISTS lab_results
(

);

CREATE TABLE IF NOT EXISTS billing
(

);

CREATE TABLE IF NOT EXISTS users
(

);

CREATE TABLE IF NOT EXISTS roles
(

);

CREATE TABLE IF NOT EXISTS user_roles
(

);

CREATE TABLE IF NOT EXISTS audit_logs
(

);

CREATE TABLE IF NOT EXISTS system_settings
(

);

CREATE TABLE IF NOT EXISTS emergency_contact_info
(
    emergency_contact_id VARCHAR(9) NOT NULL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    sex VARCHAR(10) NOT NULL,
    phone VARCHAR(12) NOT NULL,
    email VARCHAR(50) NOT NULL,
    home_address VARCHAR(255) NOT NULL
);