from sqlalchemy.orm import Session
from repository.db_config import Database

def get_db():
    SessionLocal = Database().get_session_maker()
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()