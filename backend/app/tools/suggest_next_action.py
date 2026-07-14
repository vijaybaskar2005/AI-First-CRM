"""
Suggest Next Action Tool

Uses Groq to recommend the next best action
for a Medical Representative after an HCP interaction.
"""

import json

from app.services.groq_service import GroqService

groq = GroqService()


def suggest_next_action(interaction_details: str):
    """
    Generate the next best action based on
    the interaction details.
    """

    prompt = f"""
You are an experienced Pharmaceutical Sales Manager.

Based on the interaction details below,
suggest the NEXT BEST ACTION for the Medical Representative.

Guidelines:

- Be practical.
- Keep it short.
- Recommend one or two actionable steps.
- Mention follow-up timing if appropriate.
- Mention products or materials to bring if relevant.

Return ONLY valid JSON in this format:

{{
    "next_best_action": ""
}}

Interaction Details:

{interaction_details}
"""

    response = groq.chat(prompt)

    # If GroqService already returned a dictionary
    if isinstance(response, dict):

        # If the dictionary contains a JSON string
        if "message" in response:
            try:
                return json.loads(response["message"])
            except Exception:
                return response

        return response

    # If GroqService returned a plain string
    try:
        return json.loads(response)
    except Exception:
        return {"message": response}