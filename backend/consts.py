from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# DB config used for accessing the database
db_config = {
    'host': os.environ.get("HOST"),
    'user': os.environ.get("DATABASE_USERNAME"),
    'password': os.environ.get("DATABASE_PASSWORD"),
    'database': os.environ.get("DATABASE_NAME"),
}
