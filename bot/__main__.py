import asyncio

from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

from bot import app, env
from bot.extensions import register_extensions

register_extensions(app)


async def main() -> None:
    handler = AsyncSocketModeHandler(app, env.str("SLACK_APP_TOKEN"))
    try:
        await handler.start_async()  # connects, then blocks until interrupted
    finally:
        await handler.close_async()  # "on stopping"


asyncio.run(main())
