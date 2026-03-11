from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime #importing tools to build and define db
from sqlalchemy.ext.declarative import declarative_base #gives us base class that our table model inherits from
from sqlalchemy.orm import sessionmaker #use to create sessions/connections to talk to db
import datetime #useing this to save the record for when the scan is saved

DATABASE_URL = "sqlite:///./scans.db" #tells SQLalchemy to use a SQLite file called scancs.db in the current folder

#creates engine is a fucntion from sqlclchemy, sets up how to connect
#connect_args{...} is when sqlite blocks cross-threads connections, cross-thread connection is one thread being used byu multiple thread at same time, threead is single sequence of instruction
#engien hold all this config
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ScanResult(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String, index=True)
    result = Column(Text)
    scanned_at = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)