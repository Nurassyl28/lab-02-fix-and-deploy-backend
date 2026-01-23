"""Service for loading and querying course items from JSON data."""

import json
from functools import lru_cache
from pathlib import Path
from typing import Iterable, List, Optional

from app.models.item import Item

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "course_items.json"


def _iter_item_tree(item: Item) -> Iterable[Item]:
    """Recursively iterate over an item and all its nested children.

    Args:
        item: The root item to start iteration from.

    Yields:
        Each item in the tree, starting with the root and traversing depth-first.
    """
    yield item
    if item.items:
        for child in item.items:
            yield from _iter_item_tree(child)


@lru_cache
def get_course_items() -> List[Item]:
    """Load and return all courses from the JSON data file.

    Returns:
        A list of Item objects representing all courses.

    Note:
        Results are cached using lru_cache for performance.
    """
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        raw = json.load(handle)

    return [Item.model_validate(course) for course in raw]


def find_item_by_id(item_id: str) -> Optional[Item]:
    """Find an item by its id, searching through all courses and their nested items.

    Args:
        item_id: The unique identifier of the item to find.

    Returns:
        The matching Item if found, None otherwise.
    """
    courses = get_course_items()
    for course in courses:
        # Check if looking for this course by id or type
        if course.id == item_id or course.type == item_id:
            return course

        # Search nested items by id
        for item in _iter_item_tree(course):
            if item.type == item_id:
                return item
    return None
