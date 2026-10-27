from aiohttp import web

from bot import app, env, installation_store, state_store
from bot.extensions import register_extensions

register_extensions(app)


async def on_startup(_: web.Application) -> None:
    """Create the OAuth tables on first run; existing tables are left alone."""
    await installation_store.create_tables()
    await state_store.create_tables()


# Serves Slack's requests at /slack/events, plus /slack/install and /slack/oauth_redirect
web_app = app.web_app()
web_app.on_startup.append(on_startup)
web.run_app(web_app, port=env.int("PORT", 3000))
