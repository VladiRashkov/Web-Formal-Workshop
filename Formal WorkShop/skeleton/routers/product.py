from fastapi import APIRouter, HTTPException
from data.models import Product
from services.product_service import view_product_interaction, serve_ad



product_router = APIRouter(prefix="/products")

@product_router.get("/view_product/{profile_id}/{product_id}")
def view_product(profile_id: int, product_id: int):
    return view_product_interaction(profile_id, product_id)

@product_router.get("/serve_ad/{ip_address}")
def serve_ad_endpoint(ip_address: str):
    return serve_ad(ip_address)