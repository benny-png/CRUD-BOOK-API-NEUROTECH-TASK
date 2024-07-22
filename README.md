
# Book Management API

This is a FastAPI application for managing books, including CRUD operations and file downloads.

## Features

- **Create**: Upload a new book with a file, title, author, and year.
- **Read**: Retrieve a list of books or a specific book by ID.
- **Update**: Update details of an existing book, including the file.
- **Delete**: Remove a book by ID.
- **Download**: Download the file associated with a book.

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/benny-png/CRUD-BOOK-API-NEUROTECH-TASK.git
   cd book-management-api
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Configuration

1. Ensure you have a `SessionLocal` database configuration in `src/database/connect.py`.

2. Define your database models in `src/database/models.py`.

## Running the Application

To start the FastAPI server, use:

```sh
uvicorn src.main.app:app --reload
```

The API will be available at base URL `http://localhost:8000/books`.

## API Endpoints

### Create a Book

- **Endpoint**: `POST /books/create/`
- **Description**: Upload a new book with a file, title, author, and year.
- **Form Data**:
  - `file`: The file to upload.
  - `title`: The book title.
  - `author`: The book author.
  - `year`: The year of publication.

### Read Books

- **Endpoint**: `GET /books/`
- **Description**: Retrieve a list of books.
- **Query Parameters**:
  - `skip`: Number of items to skip.
  - `limit`: Number of items to return.

### Read a Specific Book

- **Endpoint**: `GET /books/{book_id}`
- **Description**: Retrieve a book by its ID.

### Update a Book

- **Endpoint**: `PUT /books/{book_id}`
- **Description**: Update the details of an existing book.
- **Form Data**:
  - `title`: The updated book title.
  - `author`: The updated book author.
  - `year`: The updated year of publication.
  - `file`: Optional file to update.

### Delete a Book

- **Endpoint**: `DELETE /books/{book_id}`
- **Description**: Delete a book by its ID.

### Download a Book File

- **Endpoint**: `GET /books/download/{book_id}`
- **Description**: Download the file associated with a book.

## Example Requests

**Create a Book:**

```sh
curl -X POST "http://localhost:8000/books/create/" -F "file=@path/to/file" -F "title=Book Title" -F "author=Author Name" -F "year=2024"
```

**Update a Book:**

```sh
curl -X PUT "http://localhost:8000/books/{book_id}" -F "file=@path/to/file" -F "title=Updated Title" -F "author=Updated Author" -F "year=2025"
```

**Download a Book File:**

```sh
curl -X GET "http://localhost:8000/books/download/{book_id}" --output downloaded_file
```
Here’s a short README section for the DELETE endpoint:

---

## Delete a Book

- **Endpoint**: `DELETE /books/{book_id}`

```sh
curl -X DELETE "http://localhost:8000/books/{book_id}"
```

- **Description**: Remove a book from the database by its ID.

### Parameters

- **book_id** (path parameter): The ID of the book to delete.

