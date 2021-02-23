import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planeta(Base):
    __tablename__ = 'Planeta'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Planeta_props(Base):
    __tablename__ = 'Planeta_props'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('Planeta.id'))
    residentes = Column(String(250))
    periodo_orbital = Column(String(250))
    clima = Column(String(250))
    diametro = Column(String(250))
    gravedad = Column(String(250))
    poblacion = Column(String(250))
    periodo_rotacion = Column(String(250))
    superfice_acuatica = Column(String(250))
    terreno= Column(String(250))
    planeta=relationship(Planeta)

    def to_dict(self):
        return {}

class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Personajes_props(Base):
    __tablename__ = 'Personajes_props'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_personaje = Column(Integer, ForeignKey('Personajes.id'))
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    color_ojos= Column(String(250))
    color_piel = Column(String(250))
    color_cabello = Column(String(250))
    genero = Column(String(250))
    masa = Column(String(250))
    fecha_nacimiento = Column(String(250))
    creacion= Column(String(250))
    editado = Column(String(250))
    nombre = Column(String(250))
    terreno= Column(String(250))
    personajes=relationship(Personajes)

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    nombre= Column(String(250))
    id = Column(Integer, primary_key=True)
    primer_apellido= Column(String(250))
    segundo_apellido= Column(String(250))
    login= Column(String(250))

    def to_dict(self):
        return {}

class Favoritos(Base):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer,ForeignKey('Planeta.id'))
    personajes_id = Column(Integer,ForeignKey('Personajes.id'))
    usuario_id = Column(Integer,ForeignKey('Usuario.id'))
    usuario=relationship(Usuario)
    planetas=relationship(Planeta)
    personajes=relationship(Personajes)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')