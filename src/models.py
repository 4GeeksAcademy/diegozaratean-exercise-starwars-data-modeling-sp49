import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Ciudad(Base):
    __tablename__ = 'ciudad'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    bandera = Column(String(250), nullable=False)
    himno = Column(String(250), nullable=False)

class Campeonato(Base):
    __tablename__ = 'campeonato'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    premio = Column(Integer, nullable=False)
    ciudad_id = Column(Integer, ForeignKey('ciudad.id'))
    ciudad = relationship(Ciudad)


class Piloto(Base):
    __tablename__ = 'piloto'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    categoria = Column(String(250), nullable=False)

class CampeonatoPiloto(Base):
    __tablename__ = 'campeonato_piloto'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    campeonato_id = Column(Integer, ForeignKey('campeonato.id'))
    campeonato = relationship(Campeonato)
    piloto_id = Column(Integer, ForeignKey('piloto.id'))
    piloto = relationship(Piloto)



    	

 		
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
