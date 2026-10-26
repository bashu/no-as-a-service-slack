import random
from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck

from bot import REASONS


async def no_callback(ack: AsyncAck, logger: Logger) -> None:
    """The /no slash command: replies in the channel with a random reason to say no."""
    try:
        await ack(text=random.choice(REASONS), response_type="in_channel")
    except Exception:
        logger.exception("Error responding to /no command")
