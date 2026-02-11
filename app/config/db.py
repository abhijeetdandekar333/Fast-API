from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


conn = MongoClient("mongodb+srv://abhijeet_dandekar_db:abcd%401234@cluster0.npaoyco.mongodb.net")


