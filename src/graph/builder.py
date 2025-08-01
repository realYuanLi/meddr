from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing import Any, Dict, List, Optional

from .types import State
from .nodes import (
    coordinator_node,
    planner_node,
    reporter_node,
    research_team_node,
    researcher_node,
    coder_node,
    human_feedback_node,
    plan_modifier_node,
)


def _build_base_graph():
    """Build and return the base state graph with all nodes and edges."""
    builder = StateGraph(State)
    builder.add_edge(START, "coordinator")
    builder.add_node("coordinator", coordinator_node)
    builder.add_node("planner", planner_node)
    builder.add_node("reporter", reporter_node)
    builder.add_node("research_team", research_team_node)
    builder.add_node("researcher", researcher_node)
    builder.add_node("coder", coder_node)
    builder.add_node("feedback_node", human_feedback_node)
    builder.add_node("plan_modifier", plan_modifier_node)
    builder.add_edge("reporter", END)
    return builder


def build_graph_with_memory():
    """Build and return the agent workflow graph with memory."""
    memory = MemorySaver()

    builder = _build_base_graph()
    return builder.compile(checkpointer=memory)


def build_graph():
    """Build and return the agent workflow graph without memory."""
    builder = _build_base_graph()
    return builder.compile()


graph = build_graph()
