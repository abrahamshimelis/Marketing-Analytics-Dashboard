import sys
sys.path.append('../')
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
import pandas as pd
from datetime import datetime

load_dotenv()
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']
port = os.environ['PG_PORT']
database = os.environ['PG_DATABASE']

# Database connection parameters
db_params = {
    'dbname': database,
    'user': user,
    'password': password,
    'host': host,
    'port': port
}

# Connect to the database
conn = psycopg2.connect(**db_params)

if conn:
    print('Database connected successfully')
cur = conn.cursor()

csv_file_path = '../data/boa.csv' 
df = pd.read_csv(csv_file_path)

# Convert the date column to the correct format
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

id = df['id']
post_link = df['post_link']
date = df['date']
views = df['views']
post_time = df['post_time']
bank = df['bank']
time_of_day = df['time_of_day']


# Insert data into your table (adjust the table name and columns)
for index, row in df.iterrows():
    sql_query = f"INSERT INTO telegram_post_performance (id, post_link, date, views, post_time, bank, time_of_day) VALUES ({row['id']}, '{row['post_link']}', '{row['date']}', '{row['views']}', '{row['post_time']}', '{row['bank']}', '{row['time_of_day']}')"
    cur.execute(sql_query)

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()