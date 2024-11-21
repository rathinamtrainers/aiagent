from fastapi import FastAPI, HTTPException
from typing import Dict
from webapp.models.prompt_model import PromptSubmission, PromptResponse

# FastAPI instance with a title and description for Swagger UI
app = FastAPI(
    title="LLM Prompt API",
    description="API for submitting prompts and retrieving responses from an LLM simulation.",
    version="1.0.0",
    contact={
        "name": "AIAgent FAST APIs",
        "url": "http://yettocreate.com",
        "email": "support@yettocreate.com",
    },
)

# In-memory store for prompts and responses
db: Dict[int, Dict[str, str]] = {}
next_id = 1


@app.put("/submit-prompt", response_model=PromptResponse, summary="Submit a prompt to the LLM")
async def submit_prompt(prompt_data: PromptSubmission):
    """
    Handles a PUT request to submit a new prompt.
    
    This simulates interaction with an LLM (Language Learning Model) by returning a mock response.
    
    **Returns**: The ID, prompt, and a mock response.
    """
    global next_id
    prompt = prompt_data.prompt

    # Simulate LLM response (this is where you'd call the LLM service)
    response = f"Response to the prompt: {prompt}"

    # Store the prompt and response in the in-memory DB
    db[next_id] = {"prompt": prompt, "response": response}
    
    # Return the response with the prompt ID
    result = PromptResponse(id=next_id, prompt=prompt, response=response)
    next_id += 1
    return result

@app.get("/get-response/{prompt_id}", response_model=PromptResponse, summary="Get a response by prompt ID")
async def get_response(prompt_id: int):
    """
    Handles a GET request to retrieve the response for a given prompt ID.
    
    **Returns**: The prompt and the corresponding response.
    """
    if prompt_id not in db:
        raise HTTPException(status_code=404, detail="Prompt not found")

    prompt_data = db[prompt_id]
    return PromptResponse(id=prompt_id, prompt=prompt_data["prompt"], response=prompt_data["response"])
