from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()  # loads .env file


app = FastAPI()



username = os.getenv("MONGO_USERNAME")
password = quote_plus(os.getenv("MONGO_PASSWORD", ""))
host = os.getenv("MONGO_HOST")
db_name = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb+srv://{username}:{password}@{host}/{db_name}"

conn = MongoClient(MONGO_URI)
