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
        expected_format = "%Y-%m-%d %H:%M:%S"
    
        try:
            v = datetime.strptime(v.strftime("%Y-%m-%d %H:%M:%S"), expected_format)
        except ValueError:
            raise ValueError(f"Дата должна быть в формате: {expected_format}")
        
        if v > datetime.now():
            raise ValueError('Некорректная дата рождения')
        return v

class CosmogramRead(BaseModel):
    id: int
    date_of_birth: datetime
    latitude: float
    longitude: float
    planets: Dict[str, float]
    ascendant: float
    cusps: List[float]  
    aspects: List[Dict[str, (float|str)]]
    ic: float                  # IC (Imum Coeli) Какая побочная хуита
    ds: float                # DSC (Descendant) Какая побочная хуита 2
    mc: float                 # MC (Medium Coeli) Какая побочная хуита 3

    class Config:
        from_attributes = True
    