# AI-Agent Application for Retrieval-Augmented Generation (RAG)

This repository contains the source code of an AI-agent application designed to support Retrieval-Augmented Generation (RAG) with extensive flexibility and extensibility. The system is capable of interacting with various data source formats, vector databases, and Large Language Models (LLMs). Additionally, it offers API and chat-based interfaces, and is customizable for new use cases.

## Features

- **Multi-format Data Sources**: The application supports multiple types of data source formats such as PDFs, text files, HTML, and more. It is designed to be easily extendable to new formats with minimal configuration.
- **Vector Database Support**: The AI-agent is compatible with a range of vector databases (e.g., Pinecone, Weaviate, Milvus). It allows you to plug in new vector databases to meet your specific needs.
- **LLM Flexibility**: The agent works with various Large Language Models (LLMs), including open-source and proprietary models. You can extend the application to incorporate new LLMs as they become available.
- **API & Chat Interface**: It provides both API and chat interfaces for interaction with the AI-agent. The framework can be extended to support additional use cases and interfaces.

## Use Cases

- Retrieval-Augmented Generation (RAG) for summarization, Q&A, and search across structured or unstructured data.
- Domain-specific LLMs for enhanced accuracy in specialized tasks.
- Build chatbots that leverage external knowledge to deliver more contextually relevant responses.
- Easily set up customized AI-agent workflows by adding new data formats, vector databases, LLMs, and interface endpoints.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rathinamtrainers/aiagent.git
   cd aiagent
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables. Create a `.env` file in the root directory:

   ```
   VECTOR_DB_URL=your_vector_database_url
   LLM_API_KEY=your_llm_api_key
   ```
4. Run the application:

   ```bash
   python src/webapp/main.py
   ```

## Usage

### API

You can interact with the AI-agent through a REST API. Here is an example request:

```bash
curl -X POST http://localhost:5000/api/query \
-H "Content-Type: application/json" \
-d '{
  "question": "What is RAG?",
  "data_source": "path/to/your/dataset.pdf"
}'
```

### Chat Interface

The application also supports a chat interface. You can extend this feature to integrate with various messaging platforms like Slack, Telegram, or custom chatbots.

### Extensibility

The application is designed with modular components for:

- **Adding new data source formats**: Implement new data handlers in the `data_handlers/` directory.
- **Supporting new vector databases**: Add vector database integrations in the `vector_db/` directory.
- **Integrating new LLMs**: Extend LLM functionality in the `llms/` directory.
- **Adding new use cases**: Define new workflows in the `use_cases/` directory, and expose them through APIs or chat interfaces.

## Contributing

We welcome contributions!

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, feel free to contact the repository maintainers at [rajan@rathinamtrainers.com].

## Project Structure:
```
project-root/
│
├── src/
│   ├── webapp/
│   │   ├── api/
│   │   │   └── app.py               # FastAPI backend to handle prompt submission and LLM integration
│   │   ├── services/
│   │   │   └── llm_service.py       # Logic to call the LLM API and handle responses
│   │   ├── models/
│   │   │   └── prompt_model.py      # Data models for the prompt and response
│   │   ├── utils/
│   │   │   └── response_parser.py   # Utility functions to parse and format LLM responses
│   │   └── main.py                  # FastAPI entry point
│   │
│   ├── ui/
│   │   ├── streamlit_app.py         # Streamlit app to render UI and handle user interactions
│   │   └── components/
│   │       └── layout.py            # Custom UI components for Streamlit app (input box, result display)
│   │
├── config/
│   └── settings.py                  # Configuration settings (API keys, LLM settings, etc.)
│
├── tests/
│   ├── test_api.py                  # Unit tests for FastAPI endpoints
│   ├── test_llm_service.py          # Unit tests for the LLM service
│   ├── test_response_parser.py      # Unit tests for response parsing
│   └── test_integration.py          # Integration tests for end-to-end flow
│
├── docs/
│   └── README.md                    # Project documentation
│
├── .env                             # Environment variables (e.g., LLM API keys)
├── requirements.txt                 # List of dependencies (e.g., FastAPI, Streamlit, requests)
├── Dockerfile                       # Dockerfile for containerizing the application
└── Makefile                         # Build and run commands for the project
```

### Breakdown of Key Files:

#### 1. **webapp (FastAPI)** - `/src/webapp/`
   - **`api/app.py`**: FastAPI endpoint that handles user prompt submissions from the front end, processes them, and interacts with the LLM API.
   - **`services/llm_service.py`**: Service file responsible for sending the prompt to the LLM API and handling responses.
   - **`models/prompt_model.py`**: Defines data models for the prompt and LLM response structures.
   - **`utils/response_parser.py`**: Utility function to format and handle the LLM responses, along with any error handling.
   - **`main.py`**: FastAPI entry point for running the backend server.

#### 2. **Frontend (Streamlit)** - `/src/ui/`
   - **`streamlit_app.py`**: The main Streamlit app that provides the UI. This includes prompt submission, displays the result, and handles feedback mechanisms.
   - **`components/layout.py`**: Custom Streamlit components for the input form, result display, and UI styling.

#### 3. **Configuration** - `/config/settings.py`
   - Stores API keys, LLM configuration settings, and other project-wide configuration.

#### 4. **Tests** - `/tests/`
   - **`test_api.py`**: Unit tests for FastAPI endpoints.
   - **`test_llm_service.py`**: Tests the LLM service functionality.
   - **`test_response_parser.py`**: Tests the utility functions that format and parse LLM responses.
   - **`test_integration.py`**: End-to-end integration tests, ensuring the prompt submission and response display work together.

#### 5. **Documentation and Configuration**
   - **`README.md`**: Explains how to set up, run, and deploy the project.
   - **`.env`**: Stores environment variables like LLM API keys.
   - **`requirements.txt`**: Lists all dependencies (FastAPI, Streamlit, etc.).
   - **`Dockerfile`**: Defines the steps to containerize the application using Docker.
   - **`Makefile`**: Contains commands for building, running, and testing the project easily.
---
### Streamlit & FastAPI Interaction:
- **Frontend (`Streamlit`)**: Streamlit provides a simple, interactive UI where users can input prompts. The app sends this data to the FastAPI backend.
- **Backend (`FastAPI`)**: FastAPI receives the prompt from the Streamlit frontend, processes it, and sends it to the selected LLM API. Once the response is received, it’s returned to the Streamlit app for display.

Let me know if you need further refinements or more details!