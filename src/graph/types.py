import operator
from typing import Annotated, TypedDict, List, Dict, Any, Optional

from langgraph.graph import MessagesState

from src.prompts.planner_model import Plan


class State(TypedDict):
    """State type for the graph."""

    messages: List[Dict[str, Any]]
    current_plan: Optional[Plan]
    plan_iterations: int
    human_feedback: bool
    observations: List[str]
    final_report: str
