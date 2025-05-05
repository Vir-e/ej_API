from sqlalchemy.orm import Session
from repository.db_config import Database
from psycopg2 import OperationalError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status

def get_db():
    try:
        SessionLocal = Database().get_session_maker()
        db: Session = SessionLocal()
    except (SQLAlchemyError, OperationalError, Exception) as e:
        print("Error creating database session:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        )

    try:
        yield db
    finally:
        db.close()