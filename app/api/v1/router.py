from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

# Example of an async endpoint using the database
@router.get("/items/{item_id}")
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    # Example query
    # result = await db.execute(select(Item).filter(Item.id == item_id))
    # item = result.scalar_one_or_none()
    return {"item_id": item_id}