#populating the database
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Consumer,Farmer,Produce,Order

fake=Faker()

if __name__=='__main__':
    engine= create_engine('sqlite:///farmers.db')
    Session = sessionmaker(bind=engine) #creating a session
    session = Session()
    session.query(Consumer).delete() #to delete the previous records to avoid duplication
    session.query(Farmer).delete()
    session.query(Produce).delete()
    session.query(Order).delete()


print("Seeding Farmers")
#populating the farmer table with few farmers


farmers = [
    Farmer(
        name=fake.name(),
        email=fake.email(),
        phone_number= fake.phone_number(),
        city=fake.city()
    )
for i in range(10)] #creating 10 records 

#adding the session
session.add_all(farmers)
session.commit()

#adding data to the produce table
for j in range(10):
   random_farmer = random.choice(farmers)  # Select a random farmer
   produce= Produce(
         name=fake.name(),
         price=random.randint(0, 100000),
         farmer_id=random_farmer.id
   )
 
   session.add(produce)
session.commit()
        


