from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from operations import add_student, get_all_students   # ✅ changed

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
def add_student_api(data: dict):
    return add_student(data["name"], data["subject"], data["marks"])


# ✅ Get ALL students
@app.get("/students")
def get_students_api():
    return get_all_students()


# ✅ Root
@app.get("/")
def home():
    return {"message": "Backend running"}