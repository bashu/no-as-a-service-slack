import random
from logging import Logger

from slack_bolt.context.say.async_say import AsyncSay

from bot import REASONS


async def app_mention_callback(event: dict, say: AsyncSay, logger: Logger) -> None:
    """If someone mentions your bot, reply in a thread with a random reason to say no."""
    try:
        await say(random.choice(REASONS), thread_ts=event.get("thread_ts", event["ts"]))
    except Exception:
        logger.exception("Error responding to app mention")
