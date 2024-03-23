#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex
from importlib import import_module


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if cls:
            obj_of_cls = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    obj_of_cls[key] = value

            return obj_of_cls
        else:
            return self.__objects

    def delete(self, obj=None):
        ''' delete objct'''
        if obj is None:
            return
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        del self.__objects[key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.__objects.update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()

            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    cls = classes[cls_name]
                    self.all()[key] = cls(**val)
        except FileNotFoundError:
            pass

    def close(self):
        """ close the session"""
        self.reload()
