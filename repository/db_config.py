from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class Database:
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            try:
                cls._engine = create_engine("postgresql+psycopg2://v_escolar:root@localhost:5432/bookshop", pool_size=15, max_overflow=5)   # Las credenciales de la base de datos se almacenarían como variables de entorno
                cls._Session = sessionmaker(bind=cls._engine)
                cls.Base = declarative_base()
                cls.Base.metadata.create_all(cls._engine)
            except SQLAlchemyError as e:
                raise RuntimeError("Database connection error") from e
            except Exception as e:
                raise RuntimeError("Database connection error") from e
        return cls._instance
        

    def get_engine(self):
        return self._engine
    


    def get_session_maker(self):
        return self._Session