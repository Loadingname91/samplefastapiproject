# FastAPI Car Management System

This project is a FastAPI-based API for managing car information.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL database (connection string is already in the code)

## Environment Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment
3. Install required packages: `pip install fastapi sqlalchemy psycopg2-binary uvicorn`

## Running the Application

Run: `uvicorn main:app --reload`

The API will be available at `http://localhost:8000`.

## API Endpoints

- GET `/`: Welcome message
- GET `/cars`: Retrieve all cars
- GET `/cars/{id}`: Retrieve a specific car by ID
- POST `/cars`: Add new cars
- PUT `/cars/{id}`: Update a car
- DELETE `/cars/{id}`: Delete a car

## Deployment

1. Ensure PostgreSQL database is set up (already done in this case)
2. Deploy to your chosen platform
3. Run using a production ASGI server like Gunicorn

Remember to follow best practices for securing your application in a production environment.
