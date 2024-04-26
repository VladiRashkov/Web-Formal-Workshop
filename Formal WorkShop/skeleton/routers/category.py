from data.models import Category
from fastapi import APIRouter
from services import category_service

category_router = APIRouter(prefix='/categories')


@category_router.get('/')
async def get_categories(country_code: str = None):
    categories = category_service.get_categories(country_code)
    return categories