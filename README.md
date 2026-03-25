# Study Buddy AI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Orchestration-2f855a)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ed)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Manifests-326ce5)

Study Buddy AI is a Streamlit app that generates quizzes with LLMs, lets users attempt them in the browser, scores results, and exports attempts to CSV.

## Features

- Generate quiz questions from a topic and difficulty level
- Support two formats: Multiple Choice and Fill in the Blank
- Choose LLM provider (`OpenAI` or `Groq`) and model
- Use personas (`Friendly Tutor`, `Examiner`, `Encouraging Coach`) to shape question style
- Validate structured model output with retries
- Score quiz attempts and download/save results

## Tech Stack

- Python 3.10
- Streamlit
- LangChain (`langchain`, `langchain-core`)
- Provider integrations: `langchain-openai`, `langchain-groq`
- Pydantic for schemas and output validation
- Pandas for results export
- Docker for containerization
- Kubernetes + Jenkins + ArgoCD deployment workflow

## Repository Structure

```text
.
├── application.py                  # Streamlit entrypoint
├── src/
│   ├── config/settings.py          # Env-based settings
│   ├── llm/client_factory.py       # LLM client creation by provider
│   ├── generator/question_generator.py
│   ├── models/question_schemas.py
│   ├── prompts/
│   │   ├── templates.py
│   │   └── personas.py
│   ├── utils/helpers.py            # Quiz lifecycle and CSV export
│   └── common/                     # Logging + custom exceptions
├── manifests/
│   ├── deployment.yaml             # Kubernetes Deployment
│   └── service.yaml                # Kubernetes Service
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── setup.py
```

## Prerequisites

- Python 3.10+
- `pip`
- At least one API key:
  - `OPENAI_API_KEY` for OpenAI models
  - `GROQ_API_KEY` for Groq models

## Environment Variables

The app reads config from environment variables (see `src/config/settings.py`).

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | If using OpenAI | - | API key for OpenAI provider |
| `GROQ_API_KEY` | If using Groq | - | API key for Groq provider |
| `DEFAULT_PROVIDER` | No | `Groq` | Initial provider in UI |
| `DEFAULT_MODEL` | No | `llama-3.1-8b-instant` | Initial selected model |
| `DEFAULT_PERSONA` | No | `Friendly Tutor` | Initial persona |
| `TEMPERATURE` | No | `0.9` | LLM temperature |
| `MAX_RETRIES` | No | `3` | Generation retry count |

Create a `.env` file in the repo root (optional):

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
DEFAULT_PROVIDER=Groq
DEFAULT_MODEL=llama-3.1-8b-instant
DEFAULT_PERSONA=Friendly Tutor
TEMPERATURE=0.9
MAX_RETRIES=3
```

## Local Development

1. Install dependencies:

```bash
pip install -e .
```

2. Start the app:

```bash
streamlit run application.py
```

3. Open Streamlit in your browser (typically `http://localhost:8501`).

## Docker

Build:

```bash
docker build -t study-buddy-ai .
```

Run:

```bash
docker run --rm -p 8501:8501 --env-file .env study-buddy-ai
```

## Deployment Notes

- `Jenkinsfile` defines a pipeline that:
  - Builds and pushes a Docker image
  - Updates image tag in `manifests/deployment.yaml`
  - Pushes manifest updates
  - Triggers ArgoCD sync
- Kubernetes manifests are in `manifests/`
- Deployment expects secrets/environment to be configured in-cluster (for example API keys)

## Testing and Quality

There is currently no dedicated automated test or lint configuration checked into this repository. Suggested next step:

- Add `pytest` for tests
- Add `ruff` (or `flake8` + formatter) for linting/formatting


## Known Caveats

- Quiz results and logs are written to local filesystem (`results/` and `logs/`), which may need persistent storage in containerized production.

