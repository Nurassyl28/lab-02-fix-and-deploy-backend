from fastapi import APIRouter, HTTPException, Query

from app.models.item import Item
from app.services.item_service import find_item_by_id, get_course_item, list_items

router = APIRouter()


@router.get("/course", response_model=Item)
def get_course():
    return get_course_item()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = find_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
