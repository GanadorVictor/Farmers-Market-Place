import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Farmer,Produce,Order,Consumer

# define the database connection 
DATABASE_URI = 'sqlite:///restuarants.db' #path to the database

engine = create_engine(DATABASE_URI,echo=False)
 #creating the engine
Session = sessionmaker(bind=engine) #creating a session
session = Session()