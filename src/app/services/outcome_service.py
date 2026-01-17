import json
from functools import lru_cache
from pathlib import Path
from typing import Iterable, List, Optional

from app.models.outcome import Outcome, OutcomeSet

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "outcomes.json"


def _iter_outcomes(outcomes: List[Outcome]) -> Iterable[Outcome]:
    for outcome in outcomes:
        yield outcome
        if outcome.suboutcomes:
            yield from _iter_outcomes(outcome.suboutcomes)


@lru_cache
def get_outcomes() -> OutcomeSet:
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        raw = json.load(handle)
    return OutcomeSet.model_validate(raw)


def find_outcome_by_id(outcome_id: str) -> Optional[Outcome]:
    for outcome in _iter_outcomes(get_outcomes().outcomes):
        if outcome.id == outcome_id:
            return outcome
    return None

