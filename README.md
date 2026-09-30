# AI Log

Fetches a short AI/ML fact from Groq every day and logs it to `logs/YYYY-MM-DD.md`.
Runs daily at 10:00 PM IST via GitHub Actions ([.github/workflows/daily-log.yml](.github/workflows/daily-log.yml)).

## Setup

Add a repository secret named `GROQ_API_KEY` (Settings → Secrets and variables → Actions) with your Groq API key.

## Run locally

```
pip install -r requirements.txt
GROQ_API_KEY=your_key python scripts/fetch_and_log.py
```
