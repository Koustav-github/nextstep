from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "NextAction API is running properly"
    }
