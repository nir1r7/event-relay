from sqlalchemy.orm import declarative_base
from databases import Database
from app.core.config import DATABASE_URL

database = Database(DATABASE_URL)

Base = declarative_base()