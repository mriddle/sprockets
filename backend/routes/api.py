from fastapi import APIRouter
from hub.controller import send_to_hub

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Everything is working. No endpoints are implemented yet."}

@router.get("/hello-ios")
def hello_ios():
    return {"message": "Hello from backend to iOS!"}

@router.post("/hub/test")
async def make_hub_test():
    """Test the hub connection works"""
    success = await send_to_hub("test")
    return {"success": success, "action": "test"}
