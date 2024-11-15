# from typing import List, Dict
# from app.models.cosmogram import CosmogramRead
# from app.repositories.cosmogram_repository import ICosmogramRepository

# class CompatibilityService:
#     def __init__(self, cosmogramRepository: ICosmogramRepository):
#         self.cosmogram_repository = cosmogramRepository

#     async def calculate_group_compatibility(self, cosmogram_ids: List[int]) -> Dict[int, Dict[int, float]]:
#         cosmograms = await self.cosmogram_repository.get_cosmograms_by_ids(cosmogram_ids)
        
#         if len(cosmograms) < 2:
#             raise ValueError("Для анализа совместимости нужно минимум две космограммы.")
        
#         compatibility_matrix = {}
        
#         for i, cosmo1 in enumerate(cosmograms):
#             compatibility_matrix[cosmo1.id] = {}
#             for j, cosmo2 in enumerate(cosmograms):
#                 if i == j:
#                     continue
#                 score = await self.compare_cosmograms(cosmo1, cosmo2)
#                 compatibility_matrix[cosmo1.id][cosmo2.id] = score
        
#         return compatibility_matrix
    
#     async def compare_cosmograms(self, cosmo1: CosmogramRead, cosmo2: CosmogramRead) -> float:
#         score = 0.0
#         for aspect1 in cosmo1.aspects:
#             for aspect2 in cosmo2.aspects:
#                 if aspect1["aspect"] == aspect2["aspect"]:
#                     score += 1
#         return score / max(len(cosmo1.aspects), len(cosmo2.aspects))
    
#     async def calculate_average_compatibility(self, compatibility_matrix: Dict[int, Dict[int, float]]) -> Dict[int, float]:
#         average_compatibility = {}
#         for cosmo_id, scores in compatibility_matrix.items():
#             if scores:
#                 average_compatibility[cosmo_id] = sum(scores.values()) / len(scores)
#             else:
#                 average_compatibility[cosmo_id] = 0.0
#         return average_compatibility
    
#     def find_high_compatibility_groups(self, average_compatibility: Dict[int, float], threshold: float = 0.75) -> List[int]:
#         high_compatibility_ids = [cosmo_id for cosmo_id, avg_score in average_compatibility.items() if avg_score >= threshold]
#         return high_compatibility_ids
