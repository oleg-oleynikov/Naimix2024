from app.db.db import database
from app.models.cosmogram import CosmogramCreate
from app.repositories.cosmogram_repository import ICosmogramRepository
from app.db.models import Cosmogram
from datetime import datetime
from typing import Optional
from sqlalchemy import select, insert

class CosmogramRepository(ICosmogramRepository):

    async def get_cosmogram_by_date(self, date: datetime) -> Optional[Cosmogram]:
        query = select(Cosmogram).where(Cosmogram.date_of_birth == date)
        result = await database.fetch_one(query)
        if result:
            return Cosmogram(**result)
        return None

    async def create_cosmogram(self, data: CosmogramCreate) -> int:
        query = insert(Cosmogram).values(
            date=data.birth_date,
            # data=data.data
        )
        cosmogram_id = await database.execute(query)
        return cosmogram_id
