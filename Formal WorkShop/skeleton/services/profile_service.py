from data.models import Profile, Product
from data.database import insert_query, read_query, update_query


def get_profiles(country_code: str = None or None):
    if country_code:
        query = read_query("SELECT * FROM profiles WHERE country_code = '{country_code}'")
    else:
        query = read_query("SELECT * FROM profiles")
    
    return query


def get_country_codes(country_code: str = None):
    if country_code:
        country_codes = read_query("SELECT DISTINCT country_code FROM profiles WHERE country_code = ?",(country_code,))
    else:
        country_codes = read_query("SELECT DISTINCT country_code FROM profiles")
    return [code[0] for code in country_codes]


def get_profile_by_id(profile_id: int):
    profiles = read_query("SELECT * FROM profiles WHERE id = ?", (profile_id,))
    if profiles:
        return profiles[0]


def get_favourite_categories(profile_id: int):
    favourite_categories = read_query(f"""
        SELECT interests.category_id, categories.name, interests.relevance 
        FROM interests 
        JOIN categories ON interests.category_id = categories.id
        WHERE interests.profile_id = {profile_id} 
        ORDER BY interests.relevance DESC
    """)
    return favourite_categories






