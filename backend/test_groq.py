from app.services.groq_service import GroqService

groq = GroqService()

response = groq.chat("Say Hello in one sentence.")

print(response)