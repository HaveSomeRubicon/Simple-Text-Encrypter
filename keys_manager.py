import json

def reset_json(path: str):
    with open(path, 'w') as json_file:
        json_file.write('')
        json.dump({'ciphers': []}, json_file, indent=2)