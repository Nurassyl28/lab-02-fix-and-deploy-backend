from fastapi import APIRouter, HTTPException

from app.models.outcome import Outcome, OutcomeSet
from app.services.outcome_service import find_outcome_by_id, get_outcomes

router = APIRouter()


@router.get("", response_model=OutcomeSet)
def get_all_outcomes():
    return get_outcomes()


@router.get("/{outcome_id}", response_model=Outcome)
def get_outcome(outcome_id: str):
    outcome = find_outcome_by_id(outcome_id)
    if not outcome:
        raise HTTPException(status_code=404, detail="Outcome not found")
    return outcome

