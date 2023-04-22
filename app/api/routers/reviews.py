from fastapi import APIRouter
from app.database import schemas, models

router = APIRouter()

@router.post("/", response_model=schemas.Review)
async def create_review(review: schemas.ReviewCreate):

# 实现创建评价的功能
    pass


