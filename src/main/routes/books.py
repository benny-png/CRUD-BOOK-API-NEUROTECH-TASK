from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from src.database.connect import SessionLocal
from src.database.models import Book
import src.crud as crud
import src.schemas.book as schemas
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE

@router.post("/create/", response_model=schemas.Book)
def upload_book(file: UploadFile = File(...), title: str = "", author: str = "", year: int = 0, db: Session = Depends(get_db)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    db_book = Book(title=title, author=author, year=year, file_path=file_location)
    return crud.create_book(db=db, book=db_book)



# READ

@router.get("/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books



@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book



# UPDATE


@router.put("/{book_id}", response_model=schemas.Book)
# Used Form(...) to parse multipart/form-data for form fields along with file upload
def update_book(book_id: int, title: str = Form(...), author: str = Form(...), year: int = Form(...), file: UploadFile = File(None), db: Session = Depends(get_db)):
    file_path = None
    if file:
        file_location = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
        file_path = file_location
    
    db_book = crud.update_book(db=db, book_id=book_id, title=title, author=author, year=year, file_path=file_path)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# DELETE

@router.delete("/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# DOWNLOADING BOOK REQUEST

@router.get("/download/{book_id}")
def download_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    file_path = db_book.file_path
    
    print(f"Downloading book from {file_path}")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Book file not found")
    
    return FileResponse(file_path, filename=db_book.title)
