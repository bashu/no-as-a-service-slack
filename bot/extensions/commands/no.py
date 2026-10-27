import random
from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck

from bot import REASONS, blocks


async def no_callback(ack: AsyncAck, command: dict, logger: Logger) -> None:
    """The /no slash command: privately previews a random reason to send, shuffle or cancel."""
    try:
        reason = random.choice(REASONS)
        await ack(text=reason, blocks=blocks.preview(reason, command["response_url"]))
    except Exception:
        logger.exception("Error responding to /no command")
