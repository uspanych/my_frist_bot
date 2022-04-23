from sqlalchemy import MetaData, Table, String, Integer, Column, Text, select
from .data_settings import engine

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('username', String(250)),
    Column('user_id', Integer(), unique=True),
    Column('first_name', String(250))
)

