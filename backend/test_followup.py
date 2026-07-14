from app.tools.generate_followup import generate_followup

text = """
Today I visited Dr. Paul at Apollo Hospital.

We discussed GlucoCare diabetes tablets.

He requested clinical trial documents.

I promised to share product samples next Tuesday.
"""

result = generate_followup(text)

print(result)