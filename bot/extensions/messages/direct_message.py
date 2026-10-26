import random
from logging import Logger

from slack_bolt.context.say.async_say import AsyncSay

from bot import REASONS


async def is_human_direct_message(message: dict) -> bool:
    """Match DMs to the bot, skipping bots and integrations so two bots can't reply forever."""
    return message.get("channel_type") == "im" and "bot_id" not in message


async def direct_message_callback(say: AsyncSay, logger: Logger) -> None:
    """If someone DMs your bot, reply with a random reason to say no."""
    try:
        await say(random.choice(REASONS))
    except Exception:
        logger.exception("Error responding to direct message")
