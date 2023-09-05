#populating the database
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Consumer,Farmer,Produce,Orders