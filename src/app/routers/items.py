from fastapi import APIRouter, HTTPException, Query

from app.models.item import CourseMaterial, Item
from app.services.item_service import find_item_by_id, get_course_material, list_items

router = APIRouter()


@router.get("/course", response_model=CourseMaterial)
def get_course():
    """Return the full nested course structure (tree)."""
    return get_course_material()


@router.get("", response_model=list[Item])
def get_items(
    item_type: str | None = Query(
        default=None,
        alias="type",
        description="Filter by item type (intended to search across the full nested course structure).",
    )
):
    """List course material items.

    Notes:
    - Without filters, this endpoint returns the top-level items.
    - When `type` is provided, the intended behavior is to return *all* matching items
      across the full nested course structure.
    """
    return list_items(item_type)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = find_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
