from fastapi import APIRouter

router = APIRouter(prefix="/professor", tags=["professor"])

@router.get("/request")
async def get_requests():
    return {"requests": "requests"}

@router.get("/request/{id}")
async def get_requests_by_id(id:int):
    return {"requests": id}


@router.patch("/request/{id}")
async def update_status(id:int):
    return {"requests": "status"}