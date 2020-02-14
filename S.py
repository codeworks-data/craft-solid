# Single-Responsibility Principle


# First example: play with the database
from tools.Database import Database
database = Database()


def verify_and_save_client(client):
    if not isinstance(client, str):
        return False
    if len(client) == 0:
        return False
    return database.save(client)

