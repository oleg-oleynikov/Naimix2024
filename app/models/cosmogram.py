from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from typing import Dict, List, Optional


class CosmogramCreate(BaseModel): 
    birth_date: datetime
    latitude: float
    longitude: float

    @field_validator('latitude')
    def validate_latitude(cls, v):
        if not (-90 <= v <= 90):
            raise ValueError('Широта должна быть в пределах от -90 до 90')
        return v

    @field_validator('longitude')
    def validate_longitude(cls, v):
        if not (-180 <= v <= 180):
            raise ValueError('Долгота должна быть в пределах от -180 до 180')
        return v
    
    @field_validator('birth_date')
    def validate_birth_date(cls, v):
        if v > datetime.now():
            raise ValueError('Некорректная дата рождения')
        return v

class CosmogramRead(BaseModel):
    id: int
    date_of_birth: datetime
    latitude: float
    longitude: float
    planets: Optional[Dict[str, float]] 
    ascendant: Optional[float]
    cusps: Optional[List[float]]        
    aspects: Optional[Dict[str, str]]    
    ic: Optional[float]                  # IC (Imum Coeli) Какая побочная хуита
    ds: Optional[float]                  # DSC (Descendant) Какая побочная хуита 2
    mc: Optional[float]                  # MC (Medium Coeli) Какая побочная хуита 3

    class Config:
        from_attributes = True
    