from datetime import datetime, timezone
from enum import Enum

from fastapi import UploadFile
from sqlmodel import Field, SQLModel


class MediaType(Enum):
    photo = "photo"
    video = "video"


class PostBase(SQLModel):
    text: str | None = None

class Post(PostBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    filename: str | None = None
    filepath: str | None = None
    filetype: MediaType | None = None
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )

class PostPublic(PostBase):
    id: int
    filename: str | None = None
    filepath: str | None = None
    filetype: MediaType | None = None
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )
