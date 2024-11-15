from sqlalchemy import Column, DateTime, Integer, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cosmogram(Base):
    __tablename__ = "cosmogram"
    id = Column(Integer, primary_key=True)

    date_of_birth = Column(DateTime, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    planets = Column(JSON, nullable=True)
    
    ascendant = Column(Float, nullable=True)
    cusps = Column(JSON, nullable=True) 

    aspects = Column(JSON, nullable=True)
    ic = Column(Float, nullable=True)
    ds = Column(Float, nullable=True)
    mc = Column(Float, nullable=True) 