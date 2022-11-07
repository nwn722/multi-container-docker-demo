import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask


#DB queries
MESSAGES = """select greeting from messages;"""


load_dotenv()  # loads variables from .env file into environment

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)


@app.route('/hello')
def hello():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(MESSAGES)
            message=cursor.fetchone()[0]
    return {"message": message}

