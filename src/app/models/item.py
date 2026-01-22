from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel


class Item(BaseModel):
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
