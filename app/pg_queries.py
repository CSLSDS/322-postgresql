# app/pg_queries.py
## connect to elephantsql-hosted postgresql:

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env vars add them to env

DB_NAME=os.getenv('DB_NAME', default="OOPS")
DB_USER=os.getenv('DB_USER', DEFAULT='OOPS')
DB_PASSWORD=os.getenv('DB_PASSWORD', DEFAULT='OOPS')
DB_HOST=os.getenv('DB_HOST', DEFAULT-'OOPS')

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
print("cursor:", cursor)

cursor.execute('SELECT * from test_table;')

result= cursor.fetchone()
print('result:', result
