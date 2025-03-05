import json
import os

USER_DATABASE_FILE = "users.json"
ADMIN_DATABASE_FILE = "admins.json"

def load_users():
    if not os.path.exists(USER_DATABASE_FILE):
        save_users({})  # Create empty user database if not found
    try:
        with open(USER_DATABASE_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_DATABASE_FILE, "w") as file:
        json.dump(users, file, indent=4)

def load_admins():
    if not os.path.exists(ADMIN_DATABASE_FILE):
        save_admins({})  # Create empty admin database if not found
    try:
        with open(ADMIN_DATABASE_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_admins(admins):
    with open(ADMIN_DATABASE_FILE, "w") as file:
        json.dump(admins, file, indent=4)
