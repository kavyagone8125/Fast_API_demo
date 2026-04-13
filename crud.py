from sqlalchemy.orm import Session
import model

# CREATE
def create_student(db: Session, student):
    new_student = model.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# READ ALL
def get_students(db: Session):
    return db.query(model.Student).all()

# READ ONE
def get_student(db: Session, student_id: int):
    return db.query(model.Student).filter(model.Student.id == student_id).first()

# UPDATE
def update_student(db: Session, student_id: int, student):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.name = student.name
        db_student.age = student.age
        db_student.course = student.course

        db.commit()
        db.refresh(db_student)
    return db_student

# DELETE
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

