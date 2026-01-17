from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class Outcome(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: str = "outcome"

    titles: Optional[Dict[str, str]] = None
    descriptions: Optional[Dict[str, str]] = None

    suboutcomes: Optional[List[Outcome]] = None

    related_item_ids: Optional[List[str]] = None
    coverage_notes: Optional[Dict[str, str]] = None


Outcome.model_rebuild()


class OutcomeSet(BaseModel):
    outcomes: List[Outcome]

