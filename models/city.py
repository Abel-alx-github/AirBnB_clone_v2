#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship
import os
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    """places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None"""
