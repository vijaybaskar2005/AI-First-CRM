from app.tools.suggest_next_action import suggest_next_action

interaction = """
Today I met Dr. Paul at Apollo Hospital.

We discussed GlucoCare diabetes tablets.

He requested product samples.

He also asked for clinical trial documents.

Follow-up next Tuesday.
"""

result = suggest_next_action(interaction)

print(result)