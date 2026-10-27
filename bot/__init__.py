import json
import logging
from pathlib import Path

from environs import Env
from slack_bolt.app.async_app import AsyncApp
from slack_bolt.oauth.async_oauth_settings import AsyncOAuthSettings
from slack_sdk.oauth.installation_store.sqlalchemy import (
    AsyncSQLAlchemyInstallationStore,
)
from slack_sdk.oauth.state_store.sqlalchemy import AsyncSQLAlchemyOAuthStateStore
from sqlalchemy.ext.asyncio import create_async_engine

env = Env()
env.read_env()  # .env is optional; real environment variables take precedence

logging.basicConfig(level=logging.INFO)

REASONS = tuple(
    json.loads((Path(__file__).parent / "reasons.json").read_text(encoding="utf-8"))
)

SCOPES = ("app_mentions:read", "chat:write", "commands", "im:history")

# A local SQLite file by default; postgresql+asyncpg://... in production
engine = create_async_engine(
    env.str("DATABASE_URL", "sqlite+aiosqlite:///./db.sqlite3")
)

# Every workspace that installs the app gets its own bot token, stored here
installation_store = AsyncSQLAlchemyInstallationStore(
    client_id=env.str("SLACK_CLIENT_ID"), engine=engine
)
# One-time values that tie an OAuth redirect back to the install it started from
state_store = AsyncSQLAlchemyOAuthStateStore(expiration_seconds=600, engine=engine)

app = AsyncApp(
    signing_secret=env.str("SLACK_SIGNING_SECRET"),
    oauth_settings=AsyncOAuthSettings(
        client_id=env.str("SLACK_CLIENT_ID"),
        client_secret=env.str("SLACK_CLIENT_SECRET"),
        scopes=SCOPES,
        installation_store=installation_store,
        state_store=state_store,
    ),
)
