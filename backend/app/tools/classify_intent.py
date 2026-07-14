"""
Intent Classification Tool

Uses Groq to decide which LangGraph tool
should handle the user's request.
"""

import json

from app.services.groq_service import GroqService

groq = GroqService()


def classify_intent(user_message: str):
    """
    Determine which tool should handle
    the user's request.
    """

    prompt = f"""
You are the router of an AI-First Healthcare CRM.

Your job is ONLY to decide which tool should
handle the user's request.

Available tools:

1. log_interaction
2. edit_interaction
3. search_interaction
4. generate_followup
5. suggest_next_action

Examples:

User:
Today I met Dr. Paul...

Output:

{{
    "tool":"log_interaction"
}}

User:
Sorry the doctor's name is Dr. Ram

Output:

{{
    "tool":"edit_interaction"
}}

User:
Show previous interactions with Dr. Paul

Output:

{{
    "tool":"search_interaction"
}}

User:
Generate a follow-up message

Output:

{{
    "tool":"generate_followup"
}}

User:
Generate a follow-up email

Output:

{{
    "tool":"generate_followup_email"
}}

User:
Write a follow-up email to Dr. Kumaran

Output:

{{
    "tool":"generate_followup_email"
}}

User:
Draft an email for Dr. Mohan regarding Vicks-50 tablets

Output:

{{
    "tool":"generate_followup_email"
}}

User:
Compose a professional email to a doctor

Output:

{{
    "tool":"generate_followup_email"
}}

User:
Write a follow-up email to Doctor regarding previous product

Output:

{{
    "tool":"generate_followup_email"
}}

User:
Write a follow-up email to Doctor regarding previous order

Output:

{{
    "tool":"generate_followup_email"
}}

User:
What should I do next?

Output:

{{
    "tool":"suggest_next_action"
}}

Return ONLY valid JSON.

User Request:

{user_message}
"""

    response = groq.chat(prompt)

    try:
        return json.loads(response)

    except Exception:
        return {
            "tool": "log_interaction"
        }