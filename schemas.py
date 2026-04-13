#in shemas.py we do the data validation the crud data type correction check
from pydantic import BaseModel
#pydantic used for datavalidation in fastapi
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


class StudentResponse(StudentCreate):
    id: int

    class Config:   # ✅ must be inside class
        orm_mode = True
