import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    favorite_type = Column(String(50), nullable=False)
    favorite_id = Column(Integer, nullable=False)
    
    user = relationship("User", back_populates="favorites")
    favorite = relationship("FavoriteItem", back_populates="favorite")

class FavoriteItem(Base):
    __tablename__ = "favorite_items"
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    attribute1 = Column(String(100))
    attribute2 = Column(String(100))

    favorite = relationship("Favorite", back_populates="favorite")

class Character(FavoriteItem):
    __tablename__ = "characters"
    id = Column(Integer, ForeignKey("favorite_items.id"), primary_key=True)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)

class Planet(FavoriteItem):
    __tablename__ = "planets"
    id = Column(Integer, ForeignKey("favorite_items.id"), primary_key=True)
    population = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)

class Starship(FavoriteItem):
    __tablename__ = "starships"
    id = Column(Integer, ForeignKey("favorite_items.id"), primary_key=True)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)

render_er(Base, "diagram.png")
