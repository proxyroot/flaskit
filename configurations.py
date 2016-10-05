from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.py import MYSQL_CONF

DATABASE_URI = "mysql://%s:%s@%s/%s"%(
	MYSQL_CONF.username, MYSQL_CONF.password,
	MYSQL_CONF.host, MYSQL_CONF.database
)

engine = create_engine(
	DATABASE_URI,
	encoding=MYSQL_CONF.encoding,
	echo=True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()
