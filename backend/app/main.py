from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import get_db, test_database_connection

app = FastAPI(title="GameRoster AI API")


@app.get("/")
def root():
    return {
        "message": "GameRoster AI API is running"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    database_result = test_database_connection(db)

    return {
        "status": "ok",
        "database": database_result
    }