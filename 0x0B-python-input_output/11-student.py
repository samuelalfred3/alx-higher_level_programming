#!/usr/bin/python3
""" Module for storing the Student class. """

class Student:
    """ 
    Defines a student by first_name, last_name, and age.
    
    Attributes:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        
        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ 
        Retrieves a dictionary representation of a Student instance.
        
        Parameters:
        attrs (list): A list of strings representing attribute names. If attrs is a list of strings, only attribute names contained in this list must be retrieved. Otherwise, all attributes must be retrieved.
        
        Returns:
        dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
            
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        
        Parameters:
        json (dict): A dictionary where a key will be the public attribute name and a value will be the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
