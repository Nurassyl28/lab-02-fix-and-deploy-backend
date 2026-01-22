import json
from functools import lru_cache
from pathlib import Path
from typing import Iterable, List, Optional

from app.models.item import Item

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "course_items.json"


def _iter_item_tree(item: Item) -> Iterable[Item]:
    yield item
    if item.items:
        for child in item.items:
            yield from _iter_item_tree(child)

@lru_cache
def get_course_items() -> List[Item]:
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        raw = json.load(handle)

    return Item.model_validate(raw)

def find_item_by_id(item_id: str) -> Optional[Item]:
    courses = get_course_items()
    for course in courses:
        if course.id == item_id:
            return course
        
        for item in _iter_item_tree(course):
            if item.id == item_id:
                return item
    return None
