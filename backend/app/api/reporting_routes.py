# Reporting endpoints for analytics
from fastapi import APIRouter

router = APIRouter(prefix="/reports")

@router.get("/summary")
def summary():
    pass
