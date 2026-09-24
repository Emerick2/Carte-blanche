from pydantic import BaseModel, Field

class Question(BaseModel):
    question: str = Field(min_length=5)
    réponseA: str = Field(min_length=3)
    réponseB: str = Field(min_length=3)
    réponseC: str = Field(min_length=3)
    réponse: int = Field(ge=0)
    indice: str = Field(min_length=5)
    salle: int = Field(ge=1)