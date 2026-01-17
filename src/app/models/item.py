from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: str

    knowledge: Optional[Dict[str, str]] = None
    icon: Optional[str] = None
    date: Optional[datetime] = None

    titles: Optional[Dict[str, str]] = None
    descriptions: Optional[Dict[str, str]] = None
    commentaries: Optional[Dict[str, str]] = None
    values: Optional[Dict[str, str]] = None
    shows: Optional[Dict[str, int]] = None

    items: Optional[List[Item]] = None


Item.model_rebuild()


class CourseMaterial(BaseModel):
    items: List[Item]
