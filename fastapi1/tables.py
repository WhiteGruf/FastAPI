import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email= sa.Column(sa.Text, unique=True)
    username= sa.Column(sa.Text, unique=True)
    password_hash= sa.Column(sa.Text)
    '''
    user_id = sa.Column(sa.Integer, primary_key=True, index=True)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    login= sa.Column(sa.Text, unique=True)
    password_hash= sa.Column(sa.Text)
    email= sa.Column(sa.Text, unique=True)
    phone_number= sa.Column(sa.String)
    birthday_date= sa.Column(sa.Date)
    '''

class HouseList(Base):
    __tablename__ = "HouseLists"
    house_id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('Users.id'))
    house_number = sa.Column(sa.Integer)
    street = sa.Column(sa.String)
    price = sa.Column(sa.Numeric(10,2))
    description = sa.Column(sa.String)
    sold = sa.Column(sa.String)
    

class ToDoList(Base):
    __tablename__ = 'ToDoList'
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('Users.id'))
    task = sa.Column(sa.String)
    date = sa.Column(sa.Date)
    close = sa.Column(sa.String)