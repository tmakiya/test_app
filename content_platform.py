import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

UPLOAD_DIR = "uploads"
DB_PATH = "content.db"

os.makedirs(UPLOAD_DIR, exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Content(Base):
    __tablename__ = "contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    content_type = Column(String, nullable=False)
    filename = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class ContentResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    content_type: str
    filename: str

    class Config:
        orm_mode = True

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI(title="Manufacturing Content Platform")

@app.post("/contents/", response_model=ContentResponse)
async def create_content(
    title: str = Form(...),
    content_type: str = Form(...),
    description: Optional[str] = Form(None),
    file: UploadFile = File(...),
):
    if content_type not in {"video", "audio", "text", "slide"}:
        raise HTTPException(status_code=400, detail="Invalid content type")

    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    session = SessionLocal()
    db_content = Content(
        title=title,
        description=description,
        content_type=content_type,
        filename=file.filename,
    )
    session.add(db_content)
    session.commit()
    session.refresh(db_content)
    session.close()
    return db_content

@app.get("/contents/", response_model=List[ContentResponse])
def list_contents(content_type: Optional[str] = None):
    session = SessionLocal()
    query = session.query(Content)
    if content_type:
        query = query.filter(Content.content_type == content_type)
    contents = query.all()
    session.close()
    return contents

@app.get("/contents/{content_id}", response_model=ContentResponse)
def get_content(content_id: int):
    session = SessionLocal()
    content = session.query(Content).filter(Content.id == content_id).first()
    session.close()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@app.get("/contents/{content_id}/file")
def get_content_file(content_id: int):
    session = SessionLocal()
    content = session.query(Content).filter(Content.id == content_id).first()
    session.close()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    file_path = os.path.join(UPLOAD_DIR, content.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=content.filename)
