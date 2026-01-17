import json
from functools import lru_cache
from pathlib import Path
from typing import Iterable, List, Optional

from app.models.item import CourseMaterial, Item

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "course_material.json"


def _iter_items(items: List[Item]) -> Iterable[Item]:
    for item in items:
        yield item
        nested_groups = [item.items]
        for group in nested_groups:
            if group:
                yield from _iter_items(group)


@lru_cache
def get_course_material() -> CourseMaterial:
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        raw = json.load(handle)
    return CourseMaterial.model_validate(raw)


def list_items(item_type: Optional[str] = None) -> List[Item]:
    material = get_course_material()
    if not item_type:
        return material.items
    return [item for item in material.items if item.type == item_type]


def find_item_by_id(item_id: str) -> Optional[Item]:
    material = get_course_material()
    for item in _iter_items(material.items):
        if item.id == item_id:
            return item
    return None
