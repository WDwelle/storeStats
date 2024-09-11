import sqlalchemy
import psycopg2

# establish connection to the DB ../raw for csv files with data.
engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:X0-warriorX@localhost:5432/SuperMart_DB')
