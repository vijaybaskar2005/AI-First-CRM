"""
Log Interaction Tool

This tool converts a natural language conversation
into structured CRM interaction data using Groq.
"""

import json
from datetime import datetime, timedelta

from app.services.groq_service import GroqService

groq = GroqService()


def convert_natural_date(date_text: str):
    """
    Converts natural language dates into YYYY-MM-DD.
    """

    if not date_text:
        return ""

    text = date_text.strip().lower()

    today = datetime.today()

    if text == "today":
        return today.strftime("%Y-%m-%d")

    if text == "tomorrow":
        return (today + timedelta(days=1)).strftime("%Y-%m-%d")

    if text == "yesterday":
        return (today - timedelta(days=1)).strftime("%Y-%m-%d")

    weekdays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    if text.startswith("next "):

        day_name = text.replace("next ", "").strip()

        if day_name in weekdays:

            target = weekdays[day_name]

            days_ahead = target - today.weekday()

            if days_ahead <= 0:
                days_ahead += 7

            next_day = today + timedelta(days=days_ahead)

            return next_day.strftime("%Y-%m-%d")

    return date_text


def log_interaction(user_message: str):
    """
    Extract structured interaction details
    from a Medical Representative conversation.
    """

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM used by Medical Representatives.

Your job is to extract structured interaction information.

Return ONLY valid JSON.

Do NOT return markdown.

Do NOT explain anything.

If a field is not mentioned:

- sentiment = "neutral"
- interaction_type = "Meeting"
- all other missing fields = ""

Extract the following information.

{{
    "doctor_name": "",
    "hospital": "",
    "interaction_type": "Meeting",
    "visit_date": "",
    "visit_time": "",
    "products_discussed": "",
    "discussion_summary": "",
    "samples_distributed": "",
    "sentiment": "neutral",
    "outcomes": "",
    "follow_up_date": "",
    "remarks": ""
}}

Extraction Rules

1. doctor_name
Extract doctor's name.

Example:
Dr. Paul

2. hospital
Hospital or clinic name.

3. visit_date
Convert relative dates like Today, Tomorrow etc.

4. visit_time
Extract time in HH:MM (24-hour format).

Examples:

11:30 AM -> 11:30

2:15 PM -> 14:15

5. products_discussed

Return every discussed medicine.

Example:

Dimma Fever Tablet, JITY-50 Cold Tablet

6. discussion_summary

One short sentence summarizing the discussion.

7. samples_distributed

Extract exactly what samples were given.

Example:

One sample pack of Dimma

One sample pack each of Dimma and JITY-50

8. sentiment

positive

negative

neutral

If doctor showed positive interest,
return positive.

If doctor rejected or was unhappy,
return negative.

Otherwise neutral.

9. outcomes

Only include important business outcomes.

Examples:

Doctor agreed to prescribe.

Doctor requested another visit.

Doctor ordered 8 boxes.

Doctor showed positive interest.

Otherwise return empty string.

10. follow_up_date

Convert natural language dates.

11. remarks

Only additional notes not already covered.

User Conversation:

{user_message}
"""

    response = groq.chat(prompt)

    try:

        data = json.loads(response)

        data["visit_date"] = convert_natural_date(
            data.get("visit_date", "")
        )

        data["follow_up_date"] = convert_natural_date(
            data.get("follow_up_date", "")
        )

        return data

    except Exception:

        return {
            "doctor_name": "",
            "hospital": "",
            "interaction_type": "Meeting",
            "visit_date": "",
            "visit_time": "",
            "products_discussed": "",
            "discussion_summary": response,
            "samples_distributed": "",
            "sentiment": "neutral",
            "outcomes": "",
            "follow_up_date": "",
            "remarks": "JSON Parsing Failed"
        }