import os
from shutil import copyfileobj
from typing import Annotated

from fastapi import APIRouter, HTTPException, UploadFile, Form
from sqlmodel import desc, select

from ..db import UPLOAD_DIR, SessionDep
from ..models import Post, PostBase, PostPublic


router = APIRouter(prefix="/posts", tags=["posts"])


def get_filetype(filename):
    extension = os.path.splitext(filename)[1].lower()

    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".webm"]

    if extension in image_extensions:
        return "photo"
    elif extension in video_extensions:
        return "video"
    else:
        return "unknown"


@router.get("/", response_model=list[Post])
async def get_posts(session: SessionDep):
    posts = session.exec(select(Post).order_by(desc("created_at"))).all()

    return posts

@router.post("/", response_model=PostPublic)
async def create_post(session: SessionDep, text: Annotated[str, Form()], fileobj: UploadFile | None = None):
    post = Post(text=text)

    if fileobj:
        post.filename = fileobj.filename
        post.filepath = (UPLOAD_DIR / fileobj.filename).as_posix()
        post.filetype = get_filetype(fileobj.filename)

        with open(post.filepath, "wb") as buffer:
            copyfileobj(fileobj.file, buffer)

    session.add(post)
    session.commit()
    session.refresh(post)

    return post

@router.patch("/{pk}", response_model=PostPublic)
async def update_post(session: SessionDep, pk: int, text: Annotated[str, Form()]):
    db_post = session.get(Post, pk)

    if not db_post:
        HTTPException(status_code=404, detail="Post is not found!")

    db_post.text = text
    session.add(db_post)
    session.commit()
    session.refresh(db_post)

    return db_post

@router.delete("/{pk}")
async def delete_post(session: SessionDep, pk: int):
    post = session.get(Post, pk)

    if not post:
        HTTPException(status_code=404, detail="Post is not found!")

    if post.filepath:
        os.unlink(post.filepath)

    session.delete(post)
    session.commit()

    return {"Ok": True}
