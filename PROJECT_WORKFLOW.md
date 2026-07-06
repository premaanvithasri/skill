# EduGenie Project Workflow

## Epic 1: Model Selection and Architecture

### Story 1
Configure Gemini 1.5 Pro and LaMini-Flan-T5 models for the main EduGenie features.

### Purpose
These AI models will support:

- Question Answering
- Summarization
- Quiz Generation
- Learning Recommendations
- Concept Explanation

---

## Epic 2: Core Functionalities Development

### Story 1
Implement the main AI-powered educational modules.

### Modules
- Explanation Module
- QnA Module
- Quiz Module
- Summary Module
- Learning Path Module

### Story 2
Create RESTful API endpoints and connect each endpoint with the related module logic.

### Example API Endpoints
- `/ask`
- `/explain`
- `/quiz`
- `/summary`
- `/learning-path`

---

## Epic 3: Frontend Development

### Story 1
Develop a responsive frontend interface.

### Frontend Features
- Task dropdown
- Text input area
- Submit button
- Styled output section
- Responsive CSS design

### Story 2
Connect frontend forms with FastAPI backend using POST requests and show real-time AI outputs.

---

## Epic 4: Deployment

### Story 1
Deploy and run EduGenie locally using FastAPI and Uvicorn.

### Run Command
```bash
uvicorn main:app --reload
