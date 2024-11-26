from dotenv import load_dotenv
import os
load_dotenv()


POSTGRES_DATABASE = os.environ["POSTGRES_DATABASE"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = int(os.environ["POSTGRES_PORT"])
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
