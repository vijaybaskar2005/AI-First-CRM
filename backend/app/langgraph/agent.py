"""
LangGraph Agent

Routes the user's request to the appropriate AI tool.
"""

from typing import TypedDict

from langgraph.graph import StateGraph, END
from app.database.database import SessionLocal

from app.services import interaction_service

from app.tools.summarize_interactions import summarize_interactions
from app.tools.classify_intent import classify_intent
from app.tools.log_interaction import log_interaction
from app.tools.edit_interaction import edit_interaction
from app.tools.search_interaction import search_interaction
from app.tools.generate_followup import generate_followup
from app.tools.generate_followup_email import generate_followup_email

class AgentState(TypedDict):
    message: str
    tool: str
    result: dict


def decide_tool(state: AgentState):
    """
    Ask Groq which tool should handle
    the user's request.
    """

    decision = classify_intent(state["message"])

    return {
        "message": state["message"],
        "tool": decision.get("tool", "log_interaction")
    }


def route(state: AgentState):
    """
    Route to the correct node.
    """

    return state["tool"]


def process_log_interaction(state: AgentState):

    interaction = log_interaction(state["message"])

    recommendation = generate_followup(
        str(interaction)
    )

    return {
        **state,
        "result": {
            "interaction": interaction,
            "followup": recommendation,
        },
    }


def process_edit_interaction(state: AgentState):

    result = edit_interaction(state["message"])

    return {
        **state,
        "result": result,
    }


def process_search_interaction(state: AgentState):
    """
    Search previous interactions and generate
    an AI summary.
    """

    search_result = search_interaction(
        state["message"]
    )
    print("Groq Search Result:", search_result)
    print("User Message:", state["message"])

    if search_result["search_type"] != "doctor_name":

        return {
            **state,
            "result": {
                "message":
                "Currently I can summarize previous interactions by doctor name only."
            },
        }

    db = SessionLocal()

    try:

        doctor_name = search_result["value"]
        print("Searching doctor:", doctor_name)
        interactions = (
            interaction_service.get_interactions_by_doctor_name(
                db,
                doctor_name,
            )
        )

        if not interactions:

            return {
                **state,
                "result": {
                    "message":
                    "No previous interactions found."
                },
            }

        history = ""

        for interaction in interactions:

            history += f"""
Visit Date: {interaction.visit_date}

Products Discussed:
{interaction.products_discussed}

Discussion Summary:
{interaction.discussion_summary}

Samples Distributed:
{interaction.samples_distributed}

Sentiment:
{interaction.sentiment}

Outcome:
{interaction.outcomes}

Remarks:
{interaction.remarks}

----------------------------------------

"""

        summary = summarize_interactions(history)

        return {
            **state,
            "result": {
                "summary": summary
            },
        }

    finally:

        db.close()


def process_generate_followup(state: AgentState):

    result = generate_followup(state["message"])

    return {
        **state,
        "result": {
            "recommendation": result
        },
    }


def process_generate_followup_email(state: AgentState):

    result = generate_followup_email(
        state["message"]
    )

    return {
        **state,
        "result": {
            "email": result
        },
    }


graph = StateGraph(AgentState)

graph.add_node("decide_tool", decide_tool)

graph.add_node(
    "log_interaction",
    process_log_interaction,
)

graph.add_node(
    "edit_interaction",
    process_edit_interaction,
)

graph.add_node(
    "search_interaction",
    process_search_interaction,
)

graph.add_node(
    "generate_followup",
    process_generate_followup,
)

graph.add_node(
    "generate_followup_email",
    process_generate_followup_email,
)

graph.set_entry_point("decide_tool")

graph.add_conditional_edges(
    "decide_tool",
    route,
    {
        "log_interaction": "log_interaction",
        "edit_interaction": "edit_interaction",
        "search_interaction": "search_interaction",
        "generate_followup": "generate_followup",
        "generate_followup_email": "generate_followup_email",
    },
)

graph.add_edge("log_interaction", END)
graph.add_edge("edit_interaction", END)
graph.add_edge("search_interaction", END)
graph.add_edge("generate_followup", END)
graph.add_edge(
    "generate_followup_email",
    END,
)
agent = graph.compile()