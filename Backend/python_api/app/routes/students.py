from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/request")
async def post_request():
    return {"request": "request"}

@router.get("/request")
async def get_all_requests(id:int):
    return {"request": id}

@router.get("/request/{id}")
async def get_request_by_idt(id:int):
    return {"request": id}

@router.get("/hours")
async def get_hours():
    return {"requests": "status"}