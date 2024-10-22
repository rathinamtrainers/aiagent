import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part

PROJECT_ID=os.environ.get('PROJECT_ID')
LOCATION_ID=os.environ.get('LOCATION')

vertexai.init(project=PROJECT_ID, location=LOCATION_ID)

models = {
    "gemini-1.5-pro-001": "gemini-1.5-pro-001",
    "gemini-1.5-flash-001": "gemini-1.5-flash-001",
}

def get_vertexai_response(prompt, model_choice, file_uri=None):
    if file_uri:
        model_choice = "gemini-1.5-pro-001"  

    model_name = models[model_choice]
    model = GenerativeModel(model_name)

    if file_uri:
        file_part = Part.from_uri(file_uri, mime_type="application/pdf")
        contents = [file_part, prompt]
    else:
        contents = [prompt]

    response = model.generate_content(contents)
    return response.text
