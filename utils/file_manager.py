import json


def save_employee(data):
    with open("data/employees.json", "w") as file:
        json.dump(data, file, indent=4)


def load_employees():
    with open("data/employees.json", "r") as file:
        return json.load(file)
