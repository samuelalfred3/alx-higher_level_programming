#!/usr/bin/python3
import sys
import json
import os

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return json.load(f)

filename = "add_item.json"
my_list = load_from_json_file(filename)
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
