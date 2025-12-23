from pydantic import BaseModel

class AnimalCreate(BaseModel):
    name: str
    species: str
    age: int
    vaccinated: bool

class AnimalOut(AnimalCreate):
    id: int
    adopted: bool

    class Config:
        from_attributes = True

