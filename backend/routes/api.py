from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Everything is working. No endpoints are implemented yet."}
