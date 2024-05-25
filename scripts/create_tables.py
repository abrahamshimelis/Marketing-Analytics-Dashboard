import sys
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

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

# Name of the database
new_db_name = 'ethio_banks_db'

# SQL statements to create tables
table_creation_queries = [
    '''
    CREATE TABLE telegram_post_performance (
        id SERIAL PRIMARY KEY,
        post_link VARCHAR(255) UNIQUE,
        date TIMESTAMP,
        views INT,
        post_time TIME,
        bank VARCHAR(255),
        time_of_day VARCHAR(255)
    )
    ''',
    '''
    CREATE TABLE google_play_reviews (
        id SERIAL PRIMARY KEY,
        review_id VARCHAR(255) UNIQUE,
        username VARCHAR(255),
        user_image VARCHAR(255),
        likes INT,
        review_created_version VARCHAR(255),
        created_at TIMESTAMP,
        reply_content TEXT,
        replied_at TIMESTAMP,
        app_version VARCHAR(255),
        score INT,
        user_comments TEXT,,
        sentiment VARCHAR(255),
    )
    ''',
    '''
    CREATE TABLE google_play_downloads (
        id SERIAL PRIMARY KEY,
        app_id VARCHAR(255),
        date TIMESTAMP,
        downloads INT
    )
    ''',
    '''
    CREATE TABLE telegram_subscription_growth (
        id SERIAL PRIMARY KEY,
        channel_id VARCHAR(255),
        date TIMESTAMP,
        subscriber_count INT
    )
    '''
]

# Function to create a new database
def create_database(db_params, new_db_name):
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))
    cur.close()
    conn.close()

# Function to create tables in the new database
def create_tables(db_params, new_db_name, table_creation_queries):
    db_params['dbname'] = new_db_name
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    for query in table_creation_queries:
        cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

# Main function to orchestrate database and table creation
def main():
    try:
        create_database(db_params, new_db_name)
        print(f"Database '{new_db_name}' created successfully.")
        create_tables(db_params, new_db_name, table_creation_queries)
        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
