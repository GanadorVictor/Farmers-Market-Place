import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Farmer,Produce,Order,Consumer

# define the database connection 
DATABASE_URI = 'sqlite:///farmers.db' #path to the database

engine = create_engine(DATABASE_URI,echo=False)
 #creating the engine
Session = sessionmaker(bind=engine) #creating a session
session = Session()

@click.group()
def cli():
    """ Farmer Market Place"""

@cli.command()
def farmer_profile():
    """Create a new farmer profile"""
    click.echo("Enter farmer details:")
    name=click.prompt("Name")
    email= click.prompt("Enter email")
    phone_number=click.prompt("Enter phone Number")
    city=click.prompt("Enter City")

#creating a new farmer record and adding it to the database
    new_farmer=Farmer(name=name,email=email,phone_number=phone_number,city=city)
    session.add(new_farmer)
    session.commit()
    click.echo("Created new farmer profile successfully!")



if __name__ == '__main__':
    cli()
    Session = Session()