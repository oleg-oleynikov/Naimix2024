from app.db.db import database
from app.models.cosmogram import CosmogramCreate
from app.repositories.cosmogram_repository import ICosmogramRepository
from app.db.models import Cosmogram
from datetime import datetime
from typing import Optional, Dict, List
from sqlalchemy import select, insert

class CosmogramRepository(ICosmogramRepository):

    async def get_cosmogram_by_date(self, date: datetime) -> Optional[Cosmogram]:
        query = select(Cosmogram).where(Cosmogram.date_of_birth == date)
        result = await database.fetch_one(query)
        if result:
            return Cosmogram(**result)
        return None

    async def create_cosmogram(self, data: CosmogramCreate, planet_positions: Dict[str, float], cusps: List[float], aspects: List[Dict[str, float | str]]) -> int:
        query = insert(Cosmogram).values(
            date_of_birth=data.birth_date,
            latitude=data.latitude,
            longitude=data.longitude,
            planets = planet_positions,
            ascendant=cusps[0],
            cusps=cusps,
            aspects=aspects,
            ic=cusps[3],
            ds=cusps[6],
            mc=cusps[9],
        )
        cosmogram_id = await database.execute(query)
        return cosmogram_id
