from fastapi import APIRouter, HTTPException
from data.models import Category
from data.database import read_query

def get_categories(country_code: str = None):
    query = """
        SELECT c.id, c.name, SUM(i.relevance) as cumulative_relevance
        FROM categories c
        LEFT JOIN interests i ON c.id = i.category_id
        LEFT JOIN profiles p ON i.profile_id = p.id
    """
    if country_code:
        query += " WHERE p.country_code = ?"
        params = (country_code,)
    else:
        params = ()

    query += " GROUP BY c.id, c.name ORDER BY cumulative_relevance DESC"
    
    category_rows = read_query(query, params)
    categories = [Category(id=row[0], name=row[1], cumulative_relevance=row[2]) for row in category_rows]
    
    return categories