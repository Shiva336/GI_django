# Django CSV User Upload API

## Overview

This project is a simple Django REST API that allows uploading a CSV file containing user data. The API processes the file, validates each row, stores valid records in the database, and returns a summary of what worked and what failed.

---


## Features

- Upload CSV file through API
- Validates each row:
  - Name should not be empty
  - Email should be valid
  - Age should be between 0 and 120
- Skips duplicate emails (both existing DB and within CSV)
- Uses bulk insert for better performance
- Returns detailed errors for failed rows
- Includes unit tests

---

## Tech Stack

- Python
- Django
- Django REST Framework

---

## Project Structure
users/
├── models.py
├── serializers.py
├── services.py
├── utils.py
├── views.py
├── urls.py
└── tests/


- `models.py` → database schema  
- `serializers.py` → validation logic  
- `services.py` → main CSV processing logic  
- `utils.py` → helper functions (CSV parsing, etc.)  
- `views.py` → API endpoint  
- `tests/` → unit tests  

---

## Future improvements
- Move CSV processing to a background worker (e.g., Celery + Redis) for handling large files and improving API responsiveness

## Setup Instructions

Clone the repo and set up a virtual environment:

```bash
git clone <repo-url>
cd <repo>

python -m venv venv
venv\Scripts\activate   # Windows
```

## Install dependencies:

```bash 
pip install -r requirements.txt
```

# Run migrations:

```bash
python manage.py migrate
```

# Start the server:

```bash 
    python manage.py runserver
```

# API Endpoint

```bash 
    POST /api/users/upload/

    Request
    Content-Type: multipart/form-data
    Body:
    file: CSV file
    Sample Data

    You can find example files in:

    sample_data/input.csv
    sample_data/output.json
    Running Tests
    python manage.py test
    Notes / Approach
    Used serializers for validation instead of manual checks
    Separated business logic into services.py to keep views clean
    Used bulk_create for inserting multiple records efficiently
    Duplicate emails are handled without raising errors
    API continues processing even if some rows fail
    Limitations / Future Improvements
    Could add async processing for very large CSV files
```