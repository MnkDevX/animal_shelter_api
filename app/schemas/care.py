from pydantic import BaseModel

class CareCreate(BaseModel):
    animal_id: int
    description: str

class CareOut(CareCreate):
    id: int

    class Config:
        from_attributes = True

