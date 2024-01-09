#!/usr/bin/python3
""" Module for storing the class_to_json function. """

def class_to_json(obj):
    """ 
    Returns the dictionary description with simple data structure 
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.
    
    Parameters:
    obj: An instance of a Class. All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean.
    """
    return obj.__dict__
