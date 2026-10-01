from pydantic import BaseModel, Field

class Player(BaseModel):
    name: str = Field(min_length=3)
    score_salle_1: int = Field(ge=0)
    score_salle_2: int = Field(ge=0)
    score_salle_3: int = Field(ge=0)
    id_partie: str
