import json


def reset_json(path: str = 'keys.json'):
    with open(path, 'w') as json_file:
        json_file.write('')
        json.dump({'keys': []}, json_file, indent=2)