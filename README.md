# AI Orchestrator

## Overview
The AI Orchestrator is a containerized microservices system that dynamically processes user inputs using AI models. It determines the appropriate task and delegates processing to specialized services.

## Features
- **Task Routing:** The orchestrator identifies and forwards tasks to the relevant microservice.
- **Data Cleaning:** Processes user data to remove inconsistencies and validate fields.
- **Sentiment Analysis:** Analyzes user text and returns sentiment classification.
- **Containerized Deployment:** Each service runs in a separate container, orchestrated via Docker Compose.
- **Web UI:** A simple interface built with Streamlit for user interaction.

## Architecture
### Components
1. **Orchestrator (FastAPI)**:
   - Receives user input.
   - Determines the task using an AI model.
   - Sends the request to the appropriate microservice.
   
2. **Data Cleaning Service (FastAPI)**:
   - Cleans and validates structured data.

3. **Sentiment Analysis Service (FastAPI)**:
   - Analyzes the sentiment of user-provided text.

4. **Web UI (Streamlit)**:
   - Accepts user input and displays results.

### Diagram
![diagram-export-28-03-2025-18_10_16](https://github.com/user-attachments/assets/4fb75463-d7bd-4fb9-a77b-5429e1853c16)




## Setup Instructions
### Prerequisites
- Docker & Docker Compose installed
- Python 3.8+
- OpenAI API Key

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Luna7282/AI-orchestrator
   cd AI_Orchestrator
   ```

2. Create an environment file `.env` in the project root and add:
   ```sh
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. Build and start the containers:
   ```sh
   docker-compose up --build
   ```

4. Access the services:
   - **Web UI:** [http://localhost:8501](http://localhost:8501)
   - **Orchestrator API:** [http://localhost:8000](http://localhost:8000)
   
## Example Usage
1. Open the Web UI.
2. Enter a request like:
   ```
   "Can you clean this dataset? {'name': 'John  ', 'email': 'invalid', 'age': 'twenty'}"
   ```
3. The orchestrator detects the task and routes it accordingly.
4. View the processed output in the UI.

## Assumptions
- The AI model reliably determines the task from user input.
- Services return valid JSON responses.
- Users interact via the Web UI or API.

## Additional Features (If Implemented)
- Logging & Monitoring
- Extended NLP functionalities
- Improved UI design
- Use alipne images for container optimization
  
## Demo Video
![5BFE66CC-E6CE-4578-9B5E-54E88EA85ABC_1_102_o](https://github.com/user-attachments/assets/4d2c55bc-a250-4f75-a026-8f711c7f43df)



