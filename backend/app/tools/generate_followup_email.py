"""
Generate Follow-up Email Tool

Generates a professional follow-up email
for an HCP based on the user's request.
"""

from app.services.groq_service import GroqService

groq = GroqService()


def generate_followup_email(user_message: str):
    """
    Generate a professional follow-up email.

    If the user provides doctor name,
    product, or context, use it.

    Otherwise generate a general
    follow-up email.
    """

    prompt = f"""
You are an experienced Pharmaceutical CRM Assistant.

Generate a professional follow-up email for a doctor.

Instructions:

1. If the user mentions:
- doctor name
- product name
- previous order
- previous discussion
- previous visit

Use those details naturally in the email.

2. If the user simply says:

Generate follow-up email

Write follow-up mail

Generate email

then generate a generic professional follow-up email.

The email should contain:

Subject

Greeting

Body

Closing

Signature

Use this signature:

XXXXX
Medical Representative
Phone: 99999xxxxx
Email: XXXXX840@gmail.com

IMPORTANT:

Return ONLY the email.

DO NOT return JSON.

DO NOT return Markdown.

DO NOT return code blocks.

DO NOT explain anything.

Output should look exactly like this:


Subject: Follow-up Regarding Previous Order

Dear Dr. Kumar,

I hope you are doing well.

I wanted to follow up regarding the products supplied during our previous interaction.

Please let me know if additional stock is required or if you have any feedback regarding the products.

If you have any questions, feel free to contact me anytime.

Thank you for your continued trust.

Best Regards,

XXXXX
Medical Representative
Phone: 99999xxxxx
Email: XXXXX840@gmail.com


User Request:

{user_message}
"""

    return groq.chat(prompt)