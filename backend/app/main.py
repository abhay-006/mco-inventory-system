# Entry point for the FastAPI application
# Configures routers and initializes the app

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.api import auth_routes, component_routes
from app.database.session import get_db

app = FastAPI(title="MCO Inventory System")

# Include API routers
app.include_router(auth_routes.router)
app.include_router(component_routes.router)


# Root endpoint
@app.get("/")
def root():
    return {"status": "MCO system running"}


# Database connection test endpoint
@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "connected"}