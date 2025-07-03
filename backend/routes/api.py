from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Everything is working. No endpoints are implemented yet."}

@router.get("/hello-ios")
def hello_ios():
    return {"message": "Hello from backend to iOS!"}
