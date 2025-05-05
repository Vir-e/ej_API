from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, OperationalError


class Database:
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            try:
                cls._engine = create_engine("postgresql+psycopg2://v_escolar:root@localhost:5432/bookshop", pool_size=15, max_overflow=5)
                cls._Session = sessionmaker(bind=cls._engine)
                cls.Base = declarative_base()
                cls.Base.metadata.create_all(cls._engine)
            except SQLAlchemyError as e:
                print("SqlAlchemyError:", e)
                raise RuntimeError("Database connection error")
            except Exception as e:
                print("Error creating database engine:", e)
                raise RuntimeError("Database connection error!!!!!!!!!!!!!!!!!!")
        return cls._instance
        

    def get_engine(self):
        return self._engine
    


    def get_session_maker(self):
        return self._Session