import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    favorites = relationship("FavoriteItem", back_populates="user")

class FavoriteItem(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    attribute1 = Column(String(100))
    attribute2 = Column(String(100))

    character_id = Column(Integer, ForeignKey("characters.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))
    starship_id = Column(Integer, ForeignKey("starships.id"))

    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")
    starship = relationship("Starship")

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)

class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)

class Starship(Base):
    __tablename__ = "starships"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)

render_er(Base, "diagram.png")
