import json
from constants import JSON_FILE_PATH, TXT_FILE_PATH


def serialize_to_json(score_in_str: str, high_score_in_str: str):
    data = {"score": score_in_str, "high_score": high_score_in_str}
    json_string = json.dumps(data)

    with open(JSON_FILE_PATH, "a") as file:
        file.write(json_string + ",\n")


def deserialize_from_json():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            json_string = file.read()
            data = json.loads(json_string)
            print(f"Type of data is {type(data)}")
            print(f"{data=}")

    except FileNotFoundError as e:
        print(f"Error: File not found: {JSON_FILE_PATH}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON data in file: {JSON_FILE_PATH}")

def last_char_json():
    with open(JSON_FILE_PATH, "r+") as file:
        content = file.read()

        if content:
            content = content[:-2]
            file.seek(0)
            file.write(content)

        file.write("]\n")

def first_char_json():
    with open(JSON_FILE_PATH, "r+") as file:
        first_char = file.read(1)

        if not first_char or first_char.isspace():
            file.seek(0)
            file.write("[")
        else:
            file.seek(0)
            file.write(first_char)
            content = file.read()
            content = content[:-2]
            file.seek(1)
            file.write(content)
            file.write(",\n")


def serialize_to_txt(score_in_str: str, high_score_in_str: str):
    data = {"score": score_in_str, "high_score": high_score_in_str}

    with open(TXT_FILE_PATH, "a") as file:
        file.write(str(data) + "\n")


def deserialize_from_txt():
    try:
        with open(TXT_FILE_PATH, "r") as file:
            data = file.read()
            print(f"Type of data is {type(data)}")
            print(f"{data=}")

    except FileNotFoundError as e:
        print(f"Error: File not found: {TXT_FILE_PATH}")
