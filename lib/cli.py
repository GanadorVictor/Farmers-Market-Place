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
def farmer_profile(): # creating a farmer profile 
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

@cli.command()
def add_produce(): #adding a new produce
    """add new product"""
    click.echo("Enter new produce details:")
    name = click.prompt("Enter Product  name:")
    price =click.prompt("Price ",type=float)

    farmer_id =click.prompt("Enter your farmer ID")
    new_farmer = session.query(Farmer).filter_by(id=farmer_id).first() #querying the farmers table and filtering by id 

    if new_farmer: #if the output is true add the produce to the table 
        produce = Produce(name=name,price=price, farmer=new_farmer)
        session.add(produce)
        session.commit()
        click.echo("Product listed successfully.")
    else:
        click.echo("Farmer not found.")

@cli.command()
def place_order(): #placing an order as a customer
    """place order as consumer"""
    click.echo("Enter order details:")
    consumer_name= click.prompt("Your Name")
    produce_name =click.prompt("Enter the produce name you want to order")

#finding the product by name
    product = session.query(Produce).filter_by(name=produce_name).first() 

    if product:
        new_order=Order(consumer_name=consumer_name,produce_name=produce_name, produce_id=product.id, farmer_id=product.farmer.id)
        session.add(new_order)
        session.commit()
        click.echo("Order made  successfully")
    else:
        click.echo("Order not successfully made")

#list of all the order a farmer has 
@cli.command()
def list_orders():
    """viewing the orders a farmer has"""
    farmer_id =click.prompt("Enter your farmer ID")
    farmer =session.query(Farmer).filter_by(id=farmer_id).all() #querying the farmer based on the given id

    if farmer: #if the output is true


if __name__ == '__main__':
    cli()
    Session = Session()