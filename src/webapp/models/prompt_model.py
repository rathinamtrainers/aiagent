from pydantic import BaseModel

# Data model for submitting a prompt
class PromptSubmission(BaseModel):
    prompt: str

# Data model for the response
class PromptResponse(BaseModel):
    id: int
    prompt: str
    response: str
