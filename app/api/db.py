from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://movie_user:Blessed125@localhost/movie_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer,primary_key=True),
    Column('name',String(50)),
    Column('plot',String(250)),
    Column('genres',ARRAY(String)),
    Column('casts',ARRAY(String))
)

database = Database(DATABASE_URL)
