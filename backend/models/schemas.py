from pydantic import BaseModel

class Review(BaseModel):
    title: str
    body: str
    rating: str
    reviewer: str

class ReviewsResponse(BaseModel):
    reviews_count: int
    reviews: list[Review]