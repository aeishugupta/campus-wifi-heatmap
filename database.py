
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "campus_wifi_db")


def connect_database():
    if not MONGO_URI:
        print("ERROR: MONGO_URI is missing from .env")
        return None

    try:
        client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=10000
        )

        client.admin.command("ping")

        database = client[DB_NAME]

        print("Successfully connected to MongoDB Atlas!")
        print("Database:", database.name)

        return database

    except PyMongoError as error:
        print("MongoDB connection failed.")
        print("Error type:", type(error).__name__)
        print("Error code:", getattr(error, "code", None))
        return None


if __name__ == "__main__":
    db = connect_database()

    if db is not None:
        print("Connection test completed successfully.")
