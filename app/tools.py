import csv
import sqlite3
from pathlib import Path


RESOURCES_DIR = Path(__file__).parent.parent / "resources"


def read_resource(resource):
    resource_path = RESOURCES_DIR / resource

    if resource.endswith(".csv"):
        with open(resource_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    if resource == "database.sqlite":
        connection = sqlite3.connect(resource_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM systems")

        rows = cursor.fetchall()

        connection.close()

        return rows

    raise ValueError("Unknown resource")


def write_resource(resource):
    return f"Writing to resource: {resource}"


def delete_resource(resource):
    return f"Deleting resource: {resource}"


def share_resource(resource):
    return f"Sharing resource: {resource}"