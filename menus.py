from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="armando.perez.plaza@gmail.com")
session.add(User1)
session.commit()

# Menu for Hickory Maple Pub
restaurant1 = Restaurant(name="Hickory Maple Pub", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Hickory Burger",
                     description="Angus beef, cheddar, bacon & barbecue sauce",
                     price="$15.99", restaurant=restaurant1, user_id="1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Onion Rings",
                     description="Deep fried onions glazed with honey",
                     price="$7.50", restaurant=restaurant1, user_id="1")

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Sweet Potato Fries",
                     description="Sweet potato fries with honey mustard",
                     price="$5.50", restaurant=restaurant1, user_id="1")

session.add(menuItem3)
session.commit()


# Menu for Thirsty Thyme Trattoria
restaurant2 = Restaurant(name="Thirsty Thyme Trattoria", user_id="2")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Caprese Salad",
                     description="Tomatoes, mozzarella & basil",
                     price="$6.99", restaurant=restaurant2, user_id="2")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Eggplant Parmigiana",
                     description="Grilled eggplant, tomatoes & basil",
                     price="$12.99", restaurant=restaurant2, user_id="2")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Minestrone",
                     description="Pasta, beans, vegetables & tomato broth",
                     price="$6.99", restaurant=restaurant2, user_id="2")

session.add(menuItem3)
session.commit()


# Menu for The Jest Eatery
restaurant3 = Restaurant(name="The Jest Eatery", user_id="3")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(name="Chicken Salad Croissant",
                     description="Chicken salad on a croissant",
                     price="$7.50", restaurant=restaurant3, user_id="3")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Reuben Sandwich",
                     description="Corned beef, swiss, sauerkraut, rye bread",
                     price="$7.95", restaurant=restaurant3, user_id="3")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Turkey Club",
                     description="Turkey, bacon & lettuce on baguette bread",
                     price="$7.95", restaurant=restaurant3, user_id="3")

session.add(menuItem3)
session.commit()

print "Added menu items!"
