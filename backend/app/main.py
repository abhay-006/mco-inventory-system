from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine

# Import all ORM models so their tables are registered with Base.metadata
from app.models import models  # Component, LifecycleLog, etc.
from app.models import component, assembly, gun  # tables used by foreign keys
from app.services.module_b import scale_engine_model  # ScaleSnapshot

# Create database tables once, after all models are imported
Base.metadata.create_all(bind=engine)

# Import API routers
from app.api import auth_routes
from app.api import component_routes
from app.api import dashboard_routes

app = FastAPI()

# Register routers
app.include_router(auth_routes.router)
app.include_router(component_routes.router)
app.include_router(dashboard_routes.router)


@app.get("/")
def root():
    return {"message": "MCO Inventory System API Running"}










