"""Models for course items."""

from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    """A node in the course tree structure.

    Items form a tree hierarchy representing course content:
    course -> labs -> tasks -> steps.

    Attributes:
        id: Unique identifier for this item.
        type: The type of item (e.g., 'course', 'lab', 'task', 'step').
        titles: Localized titles (e.g., {'en': 'Lab 01'}).
        descriptions: Localized descriptions.
        items: Nested child items forming a tree structure.
    """

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

    items: Optional[List["Item"]] = None
