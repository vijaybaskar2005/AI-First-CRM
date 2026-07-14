from app.tools.log_interaction import log_interaction

result = log_interaction(
    """
Today I visited Dr. Paul at Apollo Hospital.

We discussed GlucoCare diabetes tablets.

He was interested in clinical trial results.

He requested samples.

Follow up next Tuesday.
"""
)

print(result)