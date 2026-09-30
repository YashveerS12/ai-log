import os
import sys
from datetime import datetime, timezone

import requests

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    sys.exit("GROQ_API_KEY environment variable is not set")

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "openai/gpt-oss-20b"

PROMPT = (
    "Share one interesting, lesser-known fact or insight about AI or machine "
    "learning. Keep it to 3-5 short lines, plain text, no headings, no markdown, "
    "no fluff."
)


def fetch_ai_content() -> str:
    response = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": PROMPT}],
            "temperature": 0.8,
            "max_tokens": 300,
            "reasoning_effort": "low",
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def write_log(content: str) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", f"{today}.md")
    with open(path, "w") as f:
        f.write(f"# AI Log — {today}\n\n{content}\n")
    return path


def main():
    content = fetch_ai_content()
    path = write_log(content)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
