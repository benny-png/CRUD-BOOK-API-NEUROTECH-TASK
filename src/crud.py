from sqlalchemy.orm import Session
from src.database.models import Book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: Book):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book_id: int, title: str, author: str, year: int, file_path: str = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.title = title
        db_book.author = author
        db_book.year = year
        if file_path:
            db_book.file_path = file_path
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
