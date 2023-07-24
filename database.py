
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, Base,CustomerUser,AdminUser,Cart

# Replace 'database_name', 'username', 'password', 'hostname' with your MySQL connection details
DATABASE_NAME = 'ecommerce'
USERNAME = 'root'
PASSWORD = 'root1234'
HOSTNAME = 'localhost'

# Create the SQLAlchemy engine
DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

