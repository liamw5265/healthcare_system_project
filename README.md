# Electronic Health Record System
## Project Overview & Problem Statement
Small web-based Electronic Health Records (EHR) worjflow system that simpulates how a clinic manages patients, appointments, encouters, clinical orders, lab results, billing, users, permissions, and operational reporting.

A small clinic has several departments that need to work with the same patient information:

- Front Desk
- Nursing
- Providers
- Billing
- IT / System Administration

Without a centralized system, the clinic could experience:

- Duplicate patient records
- Missing or incomplete appointment information
- Untracked clinical orders
- Lab results that are not reviewed
- Inconsistent workflow steps
- Staff accessing information outside their role
- Difficulty determining who changed a record
- Poor visibility into clinic performance
- Difficulty troubleshooting workflow problems

The application provides a centralized system that coordinates these workflows.

The core problem can be summarized as:

> How can a clinic reliably move patient information through multiple departments while maintaining structured workflows, secure access, traceable changes, and useful operational reporting?

---

### Role-Based Access Control (RBAC)
| Action | Front Desk | Nurse | Provider | Billing | Admin |
|---|---:|---:|---:|---:|---:|
| Search patients | Yes | Yes | Yes | Limited | Yes |
| Register patient | Yes | No | No | No | Yes |
| Schedule appointment | Yes | No | No | No | Yes |
| Check in patient | Yes | No | No | No | Yes |
| Enter vitals | No | Yes | Yes | No | Yes |
| Add diagnosis | No | No | Yes | No | Yes |
| Create order | No | No | Yes | No | Yes |
| Review results | No | No | Yes | No | Yes |
| View billing | No | No | Limited | Yes | Yes |
| Manage users | No | No | No | No | Yes |
| View audit logs | No | No | No | No | Yes |


## Tech Stack
### Frontend
- HTML
- CSS

### Backend
- Python
- FastAPI
- SQLalchemy 

### Database
- MariaDB

### Reporting
- Power BI