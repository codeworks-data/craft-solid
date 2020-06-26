# Single-Responsibility Principle


# First example: play with the database
from tools.Database import Database
database = Database()


def save_client(client):
    if verify_client(client):
        return database.save(client)
    return False


def verify_client(client):
    if not isinstance(client, str):
        return False
    if len(client) == 0:
        return False
    return True

