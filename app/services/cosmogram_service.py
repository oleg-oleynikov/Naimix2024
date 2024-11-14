from app.models.cosmogram import CosmogramCreate, CosmogramRead
from app.repositories.cosmogram_repository import ICosmogramRepository
from typing import Dict, List
import swisseph as swe 

class CosmogramService:
    def __init__(self, cosmogramRepository: ICosmogramRepository):
        self.cosmogram_repository = cosmogramRepository

    planets = {
        'Sun': swe.SUN,
        'Moon': swe.MOON,
        'Mercury': swe.MERCURY,
        'Venus': swe.VENUS,
        'Mars': swe.MARS,
        'Jupiter': swe.JUPITER,
        'Saturn': swe.SATURN,
        'Uranus': swe.URANUS,
        'Neptune': swe.NEPTUNE,
        'Pluto': swe.PLUTO,
        'Lilith': swe.OSCU_APOG,
        'Chiron': swe.CHIRON
    }
        
    async def create_cosmogram(self, cosmogram: CosmogramCreate) -> CosmogramRead:
        planet_positions = await self.calculate_planet_position(cosmogram)
        cusps = await self.calculate_houses(cosmogram)
        ascendant = cusps[0]
        ic = cusps[3]
        ds = cusps[6]
        mc = cusps[9]

        return CosmogramRead(
            id=1,
            date_of_birth=cosmogram.birth_date,
            latitude=cosmogram.latitude,
            longitude=cosmogram.longitude,
            planets=planet_positions,
            ascendant=ascendant,
            cusps=cusps,
            aspects={},
            ic=ic,
            ds=ds,
            mc=mc
        )

    async def calculate_planet_position(self, cosmogram: CosmogramCreate) -> Dict[str, float]:
        jd = swe.julday(cosmogram.birth_date.year, cosmogram.birth_date.month, cosmogram.birth_date.day,
                    cosmogram.birth_date.hour + cosmogram.birth_date.minute / 60.0)
        
        swe.set_topo(cosmogram.longitude, cosmogram.latitude, 0)

        planet_positions : Dict[str, float] = {}
        for planet_name, planet_id in self.planets.items():
            position, _ = swe.calc_ut(jd, planet_id)
            planet_positions[planet_name] = position[0]

        node_position, _ = swe.calc_ut(jd, swe.TRUE_NODE)
        planet_positions['NNode'] = node_position[0]
        planet_positions['SNode'] = (node_position[0] + 180) % 360

        return planet_positions
    
    async def calculate_houses(self, cosmogram: CosmogramCreate) -> List[float]:
        jd = swe.julday(cosmogram.birth_date.year, cosmogram.birth_date.month, cosmogram.birth_date.day,
                        cosmogram.birth_date.hour + cosmogram.birth_date.minute / 60.0)
        
        swe.set_topo(cosmogram.longitude, cosmogram.latitude, 0)

        if abs(cosmogram.latitude) > 66.5:
            hsys = b'O'
        else:
            hsys = b'P'

        cusps, _ = swe.houses(jd, cosmogram.latitude, cosmogram.longitude, hsys=hsys)
        return cusps