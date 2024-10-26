
import os
from sqlmodel import  SQLModel, Session, create_engine
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# Create the database engine
    
engine = create_engine(DATABASE_URL, echo=True)

# Dependency to get the database session
def get_session() -> Session:
    with Session(engine) as session:
        yield session

def init_db():
    """Initialize the database by creating all tables."""
    SQLModel.metadata.create_all(engine)

