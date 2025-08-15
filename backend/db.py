import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Sohan@2005",
        database="shop"
    )
