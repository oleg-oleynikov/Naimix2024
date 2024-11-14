import databases
from sqlalchemy import create_engine, MetaData
from app.core.config import settings

database = databases.Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL)
metadata.create_all(bind=engine)

# class Database:
#     instance = None

#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#             cls.instance.client = MongoClient("mongodb://localhost:27017/")
#             cls.instance.db = cls.instance.client["mydatabase"]
#         return cls.instance