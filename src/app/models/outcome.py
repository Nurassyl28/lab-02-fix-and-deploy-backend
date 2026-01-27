from typing import Dict, List, Optional
from pydantic import BaseModel

class Outcome(BaseModel):
    id: str
    type: str
    titles: Dict[str, str]
    descriptions: Dict[str, str]
    related_item_ids: Optional[List[str]] = None
    coverage_notes: Optional[Dict[str, str]] = None
    suboutcomes: Optional[List["Outcome"]] = None

    class Config:
        populate_by_name = True
