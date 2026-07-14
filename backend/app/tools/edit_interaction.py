"""
Edit Interaction Tool

Uses Groq to understand what the user wants
to modify in the current interaction.
"""

import json

from app.services.groq_service import GroqService

groq = GroqService()


def edit_interaction(user_message: str):
    """
    Extract updated interaction fields from
    natural language.
    """

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

The Medical Representative wants to correct
or update the CURRENT interaction.

Extract ONLY the fields that need to be changed.

If a field is not mentioned,
leave it as an empty string.

Return ONLY valid JSON.

Format:

{{
    "doctor_name": "",
    "hospital": "",
    "interaction_type": "",
    "visit_date": "",
    "visit_time": "",
    "products_discussed": "",
    "discussion_summary": "",
    "samples_distributed": "",
    "sentiment": "",
    "outcomes": "",
    "follow_up_date": "",
    "remarks": ""
}}

Examples

User:
Sorry, the doctor's name is Dr. Ramu.

Output:

{{
    "doctor_name":"Dr. Ramu",
    "hospital":"",
    "interaction_type":"",
    "visit_date":"",
    "visit_time":"",
    "products_discussed":"",
    "discussion_summary":"",
    "samples_distributed":"",
    "sentiment":"",
    "outcomes":"",
    "follow_up_date":"",
    "remarks":""
}}

----------------------

User:

Actually I met him at 10:45 AM and gave two sample packs.

Output:

{{
    "doctor_name":"",
    "hospital":"",
    "interaction_type":"",
    "visit_date":"",
    "visit_time":"10:45",
    "products_discussed":"",
    "discussion_summary":"",
    "samples_distributed":"Two sample packs",
    "sentiment":"",
    "outcomes":"",
    "follow_up_date":"",
    "remarks":""
}}

----------------------

Return ONLY JSON.

User Request:

{user_message}
"""

    response = groq.chat(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "doctor_name": "",
            "hospital": "",
            "interaction_type": "",
            "visit_date": "",
            "visit_time": "",
            "products_discussed": "",
            "discussion_summary": "",
            "samples_distributed": "",
            "sentiment": "",
            "outcomes": "",
            "follow_up_date": "",
            "remarks": "",
        }