from fastapi import FastAPI
from pydantic import BaseModel
from llm_access import get_vertexai_response

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str  
    vdb: str

@app.post("/get_prompt_response")
async def get_prompt_response(prompt_request: PromptRequest):
    print(f"Received prompt: {prompt_request.prompt}")
    print(f"Selected model: {prompt_request.model}")
    print(f"Selected database: {prompt_request.vdb}") 

    response = get_vertexai_response(prompt_request.prompt, prompt_request.model)  
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
