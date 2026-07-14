from app.langgraph.agent import agent

result = agent.invoke(
    {
        "message": """
Today I met Dr. John at Apollo Hospital.

We discussed CardioPlus.

Follow up next Monday.
"""
    }
)

print(result)