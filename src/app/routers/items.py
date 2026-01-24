"""Router for course items endpoints."""

from typing import List
from fastapi import APIRouter, HTTPException

from app.models.item import Item
from app.services.item_service import find_item_by_id, get_course_items

router = APIRouter()


@router.get("", response_model=List[Item])
def get_all_courses():
    """Get all courses.

    Returns:
        A list of all course items.
    """
    return get_course_items()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    """Get a specific item by its id.

    Searches through all courses and their nested items to find
    the item with the matching id.

    Args:
        item_id: The unique identifier of the item.

    Returns:
        The matching item.

    Raises:
        HTTPException: 404 if the item is not found.
    """
    item = find_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
