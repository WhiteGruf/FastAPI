from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings_w
import psycopg2
from psycopg2 import pool

engine = create_engine(
    settings_w.database_url
)

Session = sessionmaker(
    engine, 
    autocommit=False,
    autoflush=False,
)
def get_conn(execute: str):
    try:
        postgresql_pool = pool.ThreadedConnectionPool(5, 20,
            user='fastapi_admin',
            password=9986559, 
            host='localhost', 
            port = 5433,  
            database='fastapi_db')

        conn = postgresql_pool.getconn(key=None)

        if conn:
            cursor=conn.cursor()
            cursor.execute(execute)
            data = cursor.fetchall()
        return data

    except(Exception, psycopg2.DatabaseError) as error :
        raise error
    finally:
        cursor.close()
        postgresql_pool.putconn(conn)

    

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()