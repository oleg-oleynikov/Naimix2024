from abc import ABC, abstractmethod
from app.models.cosmogram import CosmogramCreate
from app.db.models import Cosmogram
from datetime import datetime
from typing import Optional

class ICosmogramRepository(ABC):

    @abstractmethod
    async def get_cosmogram_by_date(self, date: datetime) -> Optional[Cosmogram]:
        pass

    @abstractmethod
    async def create_cosmogram(self, data: CosmogramCreate) -> int:
        pass