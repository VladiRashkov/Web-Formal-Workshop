from pydantic import BaseModel


class Profile(BaseModel):
    id: int
    ip_address: str
    country_code: str
    
    @classmethod
    def from_query_result(cls, id, ip_address, country_code):
        return cls(
            id=id,
            ip_address=ip_address,
            country_code=country_code
        )


class Category(BaseModel):
    id: int
    name: str
    
    @classmethod
    def from_query_result(cls, id, name):
        return cls(
            id=id,
            name=name
        )


class Interest(BaseModel):
    profile_id: int
    product_id: int
    relevance: int
    
    @classmethod
    def from_query_result(cls, profile_id, product_id, relevance):
        return cls(
            profile_id=profile_id,
            product_id=product_id,
            relevance=relevance
        )


class Product(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
    
    @classmethod
    def from_query_result(cls, id, name, price, category_id):
        return cls(
            id=id,
            name=name,
            price=price,
            category_id=category_id
        )
