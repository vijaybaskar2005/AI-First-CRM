"""
Search Interaction Tool

Uses Groq to understand what the user wants
to search for.
"""

import json

from app.services.groq_service import GroqService

groq = GroqService()


def search_interaction(user_message: str):
    """
    Extract search filters from
    natural language.
    """

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

Your job is to understand what the user wants to search.

Return ONLY valid JSON.

Supported search types:

doctor_name

hospital

keyword

Return this format only.

{{
    "search_type": "",
    "value": ""
}}

Examples:

User:
Show my meetings with Dr Paul

Output:
{{
    "search_type":"doctor_name",
    "value":"Dr Paul"
}}

User:
Find GlucoCare discussions

Output:
{{
    "search_type":"keyword",
    "value":"GlucoCare"
}}

User:
Apollo Hospital meetings

Output:
{{
    "search_type":"hospital",
    "value":"Apollo Hospital"
}}

User Request:

{user_message}
"""

    response = groq.chat(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "search_type": "",
            "value": ""
        }