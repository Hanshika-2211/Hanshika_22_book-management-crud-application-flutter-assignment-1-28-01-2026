# API Routes Package
#
# This file contains:
# - Main API router creation
# - Route registration from different modules
# - API versioning setup
# - Common route dependencies
#
# Example structure:
# - from fastapi import APIRouter
# - from app.api.routes import example
#
# - api_router = APIRouter()
# - Include routers from different modules
# - api_router.include_router(example.router, prefix="/example") 