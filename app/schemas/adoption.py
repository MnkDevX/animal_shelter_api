from pydantic import BaseModel

class AdoptionCreate(BaseModel):
    animal_id: int
    adopter_name: str

class AdoptionOut(AdoptionCreate):
    id: int

    class Config:
        from_attributes = True

