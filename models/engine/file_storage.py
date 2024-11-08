#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models import classes


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def all(self, cls=None):
        """
        Returns a dictionary of models currently
        in storage or of a specific class
        """
        if cls is None:
            return FileStorage.__objects
        else:
            return {
                key: val for key, val in FileStorage.__objects.items()
                if isinstance(val, cls)
            }
            
    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
