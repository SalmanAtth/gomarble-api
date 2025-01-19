from fastapi import APIRouter, Query, HTTPException
from ..models.schemas import ReviewsResponse
from ..services.scraper import extract_reviews

router = APIRouter()

@router.get("/reviews", response_model=ReviewsResponse)
async def get_reviews(url: str = Query(..., description="URL of the product page")):
    try:
        reviews = await extract_reviews(url)
        return {"reviews_count": len(reviews), "reviews": reviews}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))