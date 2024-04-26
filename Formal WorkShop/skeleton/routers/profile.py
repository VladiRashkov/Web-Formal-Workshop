from fastapi import APIRouter, HTTPException, status
from data.models import Profile
from services.profile_service import get_profiles, get_country_codes, get_profile_by_id, get_favourite_categories



profile_router = APIRouter(prefix="/profiles")


@profile_router.get("/")
def all_profiles(country_code: str = None or None):
    return get_profiles(country_code)


@profile_router.get("/country_code")
def country_codes(country_code: str = None):
    return get_country_codes(country_code)

@profile_router.get("/{profile_id}")
def read_profile(profile_id: int):
    profile_info = get_profile_by_id(profile_id)
    if profile_info is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Profile not found.")
    profile = {
        "id": profile_info[0],
        "ip_address": profile_info[1],
        "country_code": profile_info[2]
    }
    favourite_categories = get_favourite_categories(profile_id)
    profile["favourite_categories"] = favourite_categories
    return profile
