import json
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from app.models.outcome import Outcome

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "outcomes.json"


def _iter_outcome_tree(outcome: Outcome) -> Iterable[Outcome]:
    """Recursively iterate over an outcome and all its nested children."""
    yield outcome
    if outcome.suboutcomes:
        for child in outcome.suboutcomes:
            yield from _iter_outcome_tree(child)


@lru_cache
def get_outcomes_data() -> Dict[str, List[Outcome]]:
    """Load and return outcomes data from the JSON file."""
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        raw = json.load(handle)
    
    # map dictionary to model
    outcomes_list = [Outcome.model_validate(o) for o in raw.get("outcomes", [])]
    return {"outcomes": outcomes_list}


def find_outcome_by_id(outcome_id: str) -> Optional[Outcome]:
    """Find an outcome by its id, searching through all outcomes and their nested items."""
    data = get_outcomes_data()
    for outcome in data["outcomes"]:
        for item in _iter_outcome_tree(outcome):
            if item.id == outcome_id:
                return item
    return None
