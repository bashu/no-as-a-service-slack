import json
import logging
from pathlib import Path

from environs import Env
from slack_bolt.app.async_app import AsyncApp

env = Env()
env.read_env()  # .env is optional; real environment variables take precedence

logging.basicConfig(level=logging.INFO)

REASONS = tuple(
    json.loads((Path(__file__).parent / "reasons.json").read_text(encoding="utf-8"))
)

app = AsyncApp(token=env.str("SLACK_BOT_TOKEN"))
