import json

def load_file(file_path):
    return open(file_path, 'r')

def file_to_str(file_path):
    return load_file(file_path).read()

def load_json_file(file_path):
    return json.load(load_file(file_path))
