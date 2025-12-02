from typing import Annotated
from pathlib import Path

from fastapi import Depends
from sqlmodel import create_engine, Session


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


engine = create_engine(
    "sqlite:///db.sqlite3",
    connect_args={"check_same_thread": False}
)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
