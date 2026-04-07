from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/students", tags=["admin"])
async def get_students():
    return {"students": "students"}

@router.get("/students/{id}", tags=["admin"])
async def get_students_by_id(id:int):
    return {"students": id}

@router.get("/stats", tags=["admin"])
async def get_stats():
    return {"requests": "requests"}

@router.patch("/request/{id}", tags=["admin"])
async def update_status(id:int):
    return {"requests": "status"}