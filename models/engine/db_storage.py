#!/usr/bin/python3
'''module db '''
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    ''' class DBStorage'''
    __engine = None
    __session = None

    def __init__(self):
        ''' init'''
        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')
        string = f"mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}"
        self.__engine = create_engine(string, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    """
    def all(self, cls=None):
        ''' fetch all obj'''
        objects = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objects.update({obj.id: obj for obj in
                               self.__session.query(cls).all()})
        return objects
    """
    def all(self, cls=None):
        """return dictionary of instance attributes
        Args:
        cls (obj): memory address of class
        Returns:
        dictionary of objects
        """
        dbobjects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
            elif cls.__name__ in classes:
                for obj in self.__session.query(cls).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        else:
            for k, v in classes.items():
                for obj in self.__session.query(v).all():
                    key = str(v.__name__) + "." + str(obj.id)
                    val = obj
                    dbobjects[key] = val
        return dbobjects

    def new(self, obj):
        ''' add new obj'''
        self.__session.add(obj)

    def save(self):
        ''' save obj to db'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' delete obj from db'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' reload the data from db'''

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        ''' close the ssion'''
        self.__session.close()
