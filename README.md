# OPSCORE — Operations Management System

**A modular Python CLI application for managing business operations, records, scheduling, and data recovery.**

## Overview

OPSCORE is a Python-based Operations Management System designed to organize essential workflows for a service-oriented business. It provides dedicated modules for employee and customer management, job management, assignment scheduling, invoicing, reporting, and system administration.

The application uses JSON-based local persistence and a modular service-oriented structure to organize business logic, reusable utilities, and data management operations.

## Features

- **Employee Management** — Manage employee records.
- **Customer Management** — Maintain customer information.
- **Job Management** — Organize and manage job records.
- **Assignment & Scheduling** — Manage job assignments and scheduling data.
- **Invoices & Payments** — Manage invoice and payment records.
- **Reports & Analytics** — Access operational reporting functionality.
- **System Management** — Inspect system information, manage directories, view logs, and access system configuration.
- **Backup & Restoration** — Create data backups and restore selected backups.
- **JSON Persistence** — Store application data in structured JSON files.
- **Application Logging** — Record system events for troubleshooting and operational tracking.
- **Data Validation** — Validate backup files before restoration.
- **Recovery Safeguards** — Create a safety backup and prepare restored data in a temporary directory before replacing active data.

## Technology Stack

- **Language:** Python
- **Data Storage:** JSON
- **Interface:** Command-Line Interface (CLI)
- **Version Control:** Git and GitHub

## Project Structure

```text
OPSCORE/
├── data/             # JSON data files
├── models/           # Data models
├── services/         # Business logic and service modules
├── utils/            # Shared utilities
├── backups/           # Backup storage
├── logs/              # Application logs
├── tests/             # Test-related files
├── main.py            # Application entry point
├── .gitignore
└── LICENSE
```

## Data Management

OPSCORE stores application records locally in JSON format. The data directory contains files for employees, customers, jobs, assignments, invoices, payments, and system configuration.

The utility modules support file management, logging, and backup operations.

## Backup & Restoration

The restoration workflow includes backup selection, required-file checks, JSON validation, safety backup creation, temporary data preparation, and directory replacement with rollback handling for certain failures.

These safeguards help reduce the risk of data loss during restoration. The workflow is not claimed to be production-hardened.

## Getting Started

### Prerequisites

- Python 3 installed
- Git installed if cloning the repository

### Installation

**1. Clone the repository**

```bash
git clone <https://github.com/arfatkhatik/opscore.git>
```

**2. Navigate to the project directory**

```bash
cd OPSCORE
```

**3. Run the application**

```bash
python main.py
```

`https://github.com/arfatkhatik/opscore.git`

## Engineering Concepts

OPSCORE explores practical Python development concepts, including modular programming, CRUD operations, JSON persistence, file handling, validation, exception handling, logging, backup and recovery workflows, and Git-based version control.

## Project Status

**Archived Learning Project**

OPSCORE is retained as a reference project demonstrating the development of a modular Python command-line application. It is intended for learning and experimentation, rather than as a production-ready enterprise system.

## License

See the [LICENSE](LICENSE) file for licensing information.
