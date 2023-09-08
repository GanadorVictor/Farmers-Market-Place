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
    while True:
        name = click.prompt("Name",default='')
        if name:
            break  # Exiting  the loop if a non-empty name is provided
        else:
            click.echo("Name cannot be empty. Please provide a name.")
    while True:
        email = click.prompt("Enter email" ,default='')
        if email:
            break  # Exiting  the loop if a non-empty email is provided
        else:
            click.echo("Email cannot be empty. Please provide an email.")
    while True:
        phone_number = click.prompt("Enter phone Number")
        if phone_number:
            if phone_number.isdigit():  # making sure its a numeric string 
                break  # Exiting the loop if a valid phone number is provided
            else:
                click.echo("Phone Number must be a numeric value.")
        else:
            click.echo("Phone Number cannot be empty. Please provide a phone number.")
    while True:
        city = click.prompt("Enter City",default='')
        if city:
            break  # Exiting  the loop if a non-empty city is provided
        else:
            click.echo("City cannot be empty. Please provide a city.")


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
    selected_farmer =session.query(Farmer).filter_by(id=farmer_id).first() #querying the farmer based on the given id

    if selected_farmer: #if the output is true
      orders = session.query(Order).filter(Order.farmer_id == selected_farmer.id).all()
    if orders:
            click.echo("List of Orders:")
            for order in orders:
                click.echo(f"Consumer: {order.consumer_name}, Product: {order.produce.name}")

#leaving a review for a product
@cli.command()
def review():
    """leaving a review for a produce"""
    produce_name=click.prompt("Enter the produce name")
    review=click.prompt("Enter a rating  for the product between 1-10",type=int)

    #checking if it's within the range
    if 1<= review <=10:
        reviewed_produce=session.query(Produce).filter_by(name=produce_name).first()
    if reviewed_produce:
        review=Produce(name=reviewed_produce.name,review=review,price=reviewed_produce.price,farmer_id=reviewed_produce.farmer_id)
        session.add(review)
        session.commit()
        click.echo("review made successfully")
    else:
        click.echo("product not found")
if __name__ == '__main__':
    cli()
    Session = Session()