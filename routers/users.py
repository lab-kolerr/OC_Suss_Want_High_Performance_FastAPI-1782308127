from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def read_users():
    return [{"user_id": "Alice"}, {"user_id": "Bob"}]