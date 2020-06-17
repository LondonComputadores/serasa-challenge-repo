from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime
import json


engine = create_engine('sqlite:///orders.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

time_created = Column(DateTime(timezone=True), server_default=func.now())
time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    cpf = Column(Integer)
    email = Column(String(50), index=True)
    phone_number = Column(Integer)
    created_at = Column(String(time_created))
    updated_at = Column(String(time_updated))

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Orders(Base):
    __tablename__='orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_description = Column(String(80))
    item_quantity = Column(Integer)
    item_price = Column(Float)
    total_value = Column(Float)
    created_at = Column(String(time_created))
    updated_at = Column(String(time_updated))
    user = relationship('Users')

    def __repr__(self):
        return '<Orders {}>'.format(self.item_description)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Sign_In(Base):
    __tablename__ = 'sign_in'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    password = Column(String(20))

    def __repr__(self):
        return '<Sign_In {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
