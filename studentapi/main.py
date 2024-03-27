from fastapi import FastAPI
import uvicorn

app = FastAPI()

students: list = [
    {"Student_ID": 1, "Name": "Waseem", "Age": 15, "Class": "4"},
    {"Student_ID": 2, "Name": "Saleem", "Age": 16, "Class": "5"},
    {"Student_ID": 3, "Name": "Qasim", "Age": 20, "Class": "4"},
    {"Student_ID": 4, "Name": "Saleem", "Age": 21, "Class": "7"},
]


@app.get("/students")
def student_list():
    return students


@app.get("/student/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["Student_ID"] == student_id:
            return student
    return {"message": "Student not found"}


@app.post("/addStudent")
def add_student(student: dict):
    students.append(
        {
            "Student_ID": student.get("student_id"),
            "Name": student.get("name"),
            "Age": student.get("age"),
            "Class": student.get("studentClass"),
        }
    )
    return students


@app.put("/student/{student_id}")
def update_student(student_id:int, studentData: dict):
    for student in students:
        if student["Student_ID"] == student_id:
            student["Name"] = studentData.get("name")
            student["Age"] = studentData.get("age")
            student["Class"] = studentData.get("studentClass")
            return students
    return {"message": "Student not found"}


@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["Student_ID"] == student_id:
            students.remove(student)
            return students
    return {"message": "Student not found"}


def start():
    uvicorn.run("studentapi.main:app", host="127.0.0.1", port=8080, reload=True)