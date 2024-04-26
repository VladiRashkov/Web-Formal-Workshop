from fastapi import FastAPI
from data.database import init_database
from routers.profile import profile_router
from routers.product import product_router
from routers.category import category_router

init_database()

app = FastAPI()
app.include_router(profile_router)
app.include_router(product_router)
app.include_router(category_router)
