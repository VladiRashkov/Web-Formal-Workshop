from data.models import Profile, Product
from data.database import insert_query, read_query, update_query
import math
from fastapi import HTTPException

def update_interest_relevance(profile_id: int, category_id: int, increase_percentage: int):
    existing_interest = read_query(
        "SELECT relevance FROM interests WHERE profile_id = ? AND category_id = ?",
        (profile_id, category_id)
    )

    if existing_interest:
        new_relevance = existing_interest[0][0] * (1 + increase_percentage / 100)
        update_query(
            "UPDATE interests SET relevance = ? WHERE profile_id = ? AND category_id = ?",
            (new_relevance, profile_id, category_id)
        )
    else:
        
        insert_query(
            "INSERT INTO interests (profile_id, category_id, relevance) VALUES (?, ?, ?)",
            (profile_id, category_id, 1)
        )

def view_product_interaction(profile_id: int, product_id: int):
    category_id = read_query('SELECT category_id FROM products WHERE id = ?', (product_id,))[0][0]

    interest = read_query('SELECT * FROM interests WHERE profile_id = ? AND category_id = ?', (profile_id, category_id))

    if interest:
        new_relevance = math.ceil(interest[0][2] * 1.05)
        update_query('UPDATE interests SET relevance = ? WHERE profile_id = ? AND category_id = ?', (new_relevance, profile_id, category_id))
    else:
        insert_query('INSERT INTO interests(category_id, profile_id, relevance) VALUES (?, ?, ?)', (category_id, profile_id, 1))

    product = get_product_by_id(product_id)
    return {"product": product, "message": "Interest updated successfully"}


        
def get_product_by_id(product_id: int):
    product = read_query("SELECT * FROM products WHERE id = ?", (product_id,))
    if product:
        return Product.from_query_result(*product[0])
    else:
        return None
    
    
def serve_ad(ip_address: str):
   
    profile_query = read_query('SELECT id FROM profiles WHERE ip_address = ?', (ip_address,))
    
    
    if profile_query:
        profile_id = profile_query[0][0]
        
       
        interests = read_query('SELECT category_id FROM interests WHERE profile_id = ? ORDER BY relevance DESC LIMIT 3', (profile_id,))
        
        if interests:
            interest_category_ids = [i[0] for i in interests]
            interest_category_ids += [interest_category_ids[-1]] * (3 - len(interest_category_ids))
            product_query = read_query('SELECT * FROM products WHERE category_id IN (?, ?, ?) ORDER BY RANDOM() LIMIT 1', interest_category_ids)
        else:
            product_query = read_query('SELECT * FROM products ORDER BY RANDOM() LIMIT 1')
        
        if product_query:
            product = product_query[0]
            return Product(id=product[0], name=product[1], price=product[2], category_id=product[3])
        else:
            raise HTTPException(status_code=404, detail="No products found")
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

