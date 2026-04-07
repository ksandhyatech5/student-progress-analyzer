from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import collection

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Add student
@app.post("/student")
def add_student(data: dict):
    collection.insert_one(data)
    return {"message": "Student added"}

# ✅ Get ALL students
@app.get("/students")
def get_students():
    students = []

    data = list(collection.find())
    print("🔥 TOTAL FROM DB:", len(data))   # DEBUG

    for student in data:
        student["_id"] = str(student["_id"])
        students.append(student)

    return students

# ✅ Root
@app.get("/")
def home():
    return {"message": "Backend running"}