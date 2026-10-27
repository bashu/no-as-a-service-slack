import json
import random
from logging import Logger

from slack_bolt.context.ack.async_ack import AsyncAck
from slack_bolt.context.respond.async_respond import AsyncRespond
from slack_sdk.webhook.async_client import AsyncWebhookClient

from bot import REASONS, blocks


async def send_callback(
    ack: AsyncAck, action: dict, body: dict, respond: AsyncRespond, logger: Logger
) -> None:
    """Send button: post the previewed reason to the channel and remove the preview."""
    await ack()
    try:
        value = json.loads(action["value"])
        reason = value["reason"]
        response = await AsyncWebhookClient(value["response_url"]).send(
            text=reason,
            blocks=blocks.sent(reason, body["user"]["id"]),
            response_type="in_channel",
        )
        if response.status_code != 200:
            logger.error(
                "Posting reason failed: %s %s", response.status_code, response.body
            )
            return
        await respond(delete_original=True)
    except Exception:
        logger.exception("Error sending reason")


async def shuffle_callback(
    ack: AsyncAck, action: dict, respond: AsyncRespond, logger: Logger
) -> None:
    """Shuffle button: replace the preview with another random reason."""
    await ack()
    try:
        reason = random.choice(REASONS)
        await respond(
            text=reason,
            blocks=blocks.preview(reason, action["value"]),
            replace_original=True,
        )
    except Exception:
        logger.exception("Error shuffling reason")


async def cancel_callback(ack: AsyncAck, respond: AsyncRespond, logger: Logger) -> None:
    """Cancel button: remove the preview."""
    await ack()
    try:
        await respond(delete_original=True)
    except Exception:
        logger.exception("Error cancelling reason")
