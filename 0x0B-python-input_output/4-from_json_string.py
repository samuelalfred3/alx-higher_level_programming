#!/usr/bin/python3
"""
Module to convert JSON string to Python object.
"""

import json

def from_json_string(my_str):
    """
    Function to convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

# If this module is run as the main program
if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
