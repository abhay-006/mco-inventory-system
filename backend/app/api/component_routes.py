# Component management endpoints
from fastapi import APIRouter

router = APIRouter(prefix="/components")

@router.get("/")
def list_components():
    pass
