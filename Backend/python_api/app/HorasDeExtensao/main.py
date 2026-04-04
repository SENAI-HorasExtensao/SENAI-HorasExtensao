from fastapi import FastAPI
from routes import auth, admin, students, professors

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(students.router)
app.include_router(professors.router)