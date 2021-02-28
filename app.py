from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
####from data import teachers_info
import json
import pandas as pd



categories_from_excel = pd.read_excel('database_download.xlsx', sheet_name = 'categories')
meals_from_excel = pd.read_excel('database_download.xlsx', sheet_name = 'meals')


print((categories_from_excel["title"]))
#print(meals_from_excel["title"])



app = Flask(__name__)
app.secret_key = "randomstring"
# Это создаст базу в оперативной памяти, которая очистится после завершения программы.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
####app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


#db.create_all()



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String)
    password = db.Column(db.String)
    orders = db.relationship("Order", back_populates='user')


####!!!!!!!!!!!!!!!!!!!!!!#########
association_table = db.Table('association',
                             db.Column('meal_id', db.Integer, db.ForeignKey('meals.id')),
                             db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
                             )

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    summ = db.Column(db.Float)
    status = db.Column(db.String)
    mail = db.Column(db.String)
    phone = db.Column(db.String)
    adresses = db.Column(db.String)
    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    meals = db.relationship(
        "Meals", secondary=association_table, back_populates="meals"
    )

    ####    –– список блюд в заказе(можно через запятую, можно many2many)

class Meals(db.Model):
    __tablename__ = 'meals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    price = db.Column(db.Float)
    description = db.Column(db.String, unique=True)
    picture = db.Column(db.String, unique=True)
    category = db.relationship("Category")
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    orders = db.relationship(
        "Order", secondary=association_table, back_populates="orders"
    )



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    meals = db.relationship("Meals", back_populates='category')




#number = int(input())
for i in range(len(meals_from_excel["title"])):
    dish = Meals(title=(meals_from_excel["title"])[i],
                     description=(meals_from_excel["description"])[i],
                      picture=(meals_from_excel["picture"])[i],
                      price=(meals_from_excel["price"])[i])
 #                   category=(meals_from_excel["category"])[i],
  #                  )
    db.session.add(dish)
    db.session.commit()




#teacher = Teacher(name=(teachers[1])["name"],
#                  about=(teachers[1])["about"],
 #               rating=(teachers[1])["rating"],
 #               picture=(teachers[1])["picture"],
 #                 price=(teachers[1])["price"])

#db.session.add(teacher)
#db.session.commit()

#dishes = Meals.query.all()

#for dish in dishes:
 #   print(dishes.title+" " +dishes.description)




