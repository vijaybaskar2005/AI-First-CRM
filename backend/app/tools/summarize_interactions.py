"""
Interaction Summary Tool

Summarizes previous HCP interactions using Groq.
"""

from app.services.groq_service import GroqService

groq = GroqService()


def summarize_interactions(history: str):
    """
    Generate a professional CRM interaction summary.
    """

    prompt = f"""
You are an experienced Pharmaceutical CRM Assistant.

Below is the interaction history of ONE doctor.

Your task is to generate a professional CRM summary.

IMPORTANT RULES:

Do NOT return JSON.

Do NOT use markdown code blocks.

Return plain text only.

Use EXACTLY the following format.

📋 Interaction Summary

Doctor:
<Doctor Name>

Visits:
<Total Visits>

Visit Dates
• 10 Jul 2026
• 11 Jul 2026
• 12 Jul 2026

Products Discussed
• Product 1
• Product 2

Overall Sentiment
Positive / Neutral / Negative

Samples Distributed
Yes or No

Important Outcomes
• Outcome 1
• Outcome 2

Recommended Next Action
One concise recommendation for the Medical Representative.

Keep the summary short, clean and professional.

Interaction History:

{history}
"""

    return groq.chat(prompt)