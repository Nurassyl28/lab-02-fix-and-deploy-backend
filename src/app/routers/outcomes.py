from typing import Dict, List
from fastapi import APIRouter, HTTPException

from app.models.outcome import Outcome
from app.services.outcome_service import get_outcomes_data, find_outcome_by_id

router = APIRouter()


@router.get("", response_model=Dict[str, List[Outcome]])
def get_all_outcomes():
    """Get all learning outcomes.
    
    Returns:
        A dictionary containing a list of all outcomes.
    """
    return get_outcomes_data()


@router.get("/{outcome_id}", response_model=Outcome)
def get_outcome(outcome_id: str):
    """Get a specific outcome by its id.
    
    Searches through the outcome tree to find the matching id.
    
    Args:
        outcome_id: The unique identifier of the outcome.
        
    Returns:
        The matching outcome.
        
    Raises:
        HTTPException: 404 if the outcome is not found.
    """
    outcome = find_outcome_by_id(outcome_id)
    if not outcome:
        raise HTTPException(status_code=404, detail="Outcome not found")
    return outcome
