"""
Generate Follow-up Tool

Uses Groq to generate a professional
follow-up message after an HCP interaction.
"""

from app.services.groq_service import GroqService

groq = GroqService()


def generate_followup(interaction_details: str):
    """
    Generate a professional follow-up
    message for the medical representative.
    """

    prompt = f"""
You are an experienced Pharmaceutical Sales Assistant.

A Medical Representative has just completed an interaction with a doctor.

Generate a professional follow-up recommendation for the Medical Representative.

The recommendation should:

- Suggest what to discuss during the next interaction.
- Mention products discussed previously.
- Mention any sample packs provided.
- Mention any promised follow-up if available.
- Suggest the next conversation naturally.
- Keep it concise (3-5 sentences).
- Do NOT write an email.
- Do NOT greet the doctor.
- Speak directly to the Medical Representative.

Interaction Details:

{interaction_details}

Return ONLY the recommendation.
"""

    return groq.chat(prompt)