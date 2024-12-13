# FastAPI PostgreSQL Backend

A production-ready FastAPI backend with PostgreSQL database integration, SQLAlchemy ORM, and Alembic migrations.

## Prerequisites

- Python 3.11+
- PostgreSQL
- pip

## Local Development Setup

1. Clone the repository
```bash
git clone https://github.com/dev-vishnuraj/fastapi-boilerplate-template.git
cd fastapi-boilerplate-template
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up your PostgreSQL database

```bash
createdb your_database_name
```

5. Create `.env` file in the root directory and configure your environment variables
```env
DATABASE_URL=postgresql://user:password@localhost:5432/your_database_name
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

6. Run database migrations
```bash
alembic upgrade head
```

7. Start the development server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI documentation at `http://localhost:8000/docs`
- ReDoc documentation at `http://localhost:8000/redoc`

## Running Tests

```bash
pytest
```

## Project Structure

```
app/
├── api/
│   └── v1/
├── core/
├── crud/
├── db/
├── models/
└── schemas/
migrations/
├── versions/
└── env.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
