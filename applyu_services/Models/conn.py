import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database crentials
user = 'DevData1'
password = 'applyudev'
host = '8.218.238.147'
port = 3306
database = 'applyu_database'

# database location
url = ("mariadb+mariadbconnector://{0}:{1}@{2}:{3}/{4}".format(
            user,password,host,port,database))

# Open to collect database
engine = create_engine(url)

# Data binding
session = sessionmaker(bind=engine)
