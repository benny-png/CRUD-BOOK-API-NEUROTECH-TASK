from pydantic import BaseModel

# Base class containing common fields for book models
class BookBase(BaseModel):
    title: str
    author: str
    year: int

# Model used when creating a new book, inherits from BookBase
class BookCreate(BookBase):
    pass

# Model used for the response, inherits from BookBase
class Book(BookBase):
    id: int
    file_path: str = None  # Optional field for the file path

    class Config:
        orm_mode = True  # Enable compatibility with ORM models
