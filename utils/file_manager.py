import json


def save_employee(data):
    with open("data/employees.json", "w") as file:
        json.dump(data, file, indent=4)


def load_employees():
    with open("data/employees.json", "r") as file:
        return json.load(file)


def save_customer(data):
    with open("data/customers.json", "w") as file:
        json.dump(data,file, indent=4)

def load_customers():
    with open("data/customers.json", "r") as file:
        return json.load(file)

def save_jobs(data):
    with open("data/jobs.json", "w") as file:
        json.dump(data, file, indent=4)

def load_jobs():
    with open("data/jobs.json", "r") as file:
        return json.load(file)

def save_assignments(data):
    with open("data/assignments.json", "w") as file:
        json.dump(data, file, indent = 4)

def load_assignments():
    with open("data/assignments.json", "r") as file:
        return json.load(file)

def save_invoices(data):
    with open("data/invoices.json", "w") as file:
        json.dump(data, file, indent = 4)

def load_invoices():
    with open("data/invoices.json", "r") as file:
        return json.load(file)