from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    return {"message": "Welcome back"}
@router.post("/register")
def login():
    return {"message": "Welcome back"}
@router.get("/refresh_tkn")
def refresh_tkn():
    return {"message": "Welcome back"}
