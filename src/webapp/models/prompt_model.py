import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project='engaged-reducer-432905-c5', location='asia-east1')

models = {
    "gemini-1.5-pro-001": "gemini-1.5-pro-001",
    "gemini-1.5-flash-001": "gemini-1.5-flash-001",
}

def get_vertexai_response(prompt, model_choice):
    model_name = models[model_choice]
    model = GenerativeModel(model_name)

    response = model.generate_content([prompt])
    print(response.text)
    return response.text