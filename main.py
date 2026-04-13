from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import model, schemas, crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/students/", response_model=schemas.StudentResponse)
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# READ ALL
@app.get("/students/")
def read_all(db: Session = Depends(get_db)):
    return crud.get_students(db)

# READ ONE
@app.get("/students/{student_id}")
def read_one(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# UPDATE
@app.put("/students/{student_id}")
def update(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

# DELETE
@app.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Deleted successfully"}
