from typing import Dict
from core.utils.classes import Repository
from core.utils.filters_characters import remove_excess_spaces
from modules.sports.models import FavoriteSport, Sports



class SportsRepository(Repository):
    """
    Responsável por lidar com a persistência e interação com a camada de armazenamento de dados,
    com relación a unidades de medidas.
    """

    model = Sports

    @classmethod
    def update_payload(cls, *, payload: Dict, last_user_id: int, **kwargs) -> Dict:
        """
        Método responsável por atualizar o payload, antes de persistir os dados no BD.
        """
        updated_payload: Dict = super().update_payload(
            payload=payload,
            last_user_id=last_user_id,
        )

        if (name := updated_payload.pop("name", None)) is not None:
            updated_payload.update({"name": remove_excess_spaces(name).upper()})

        return updated_payload

class FavoriteSportRepository(Repository):
    model = FavoriteSport