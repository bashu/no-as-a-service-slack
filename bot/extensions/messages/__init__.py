from slack_bolt.app.async_app import AsyncApp

from .direct_message import direct_message_callback, is_human_direct_message


def register(app: AsyncApp) -> None:
    app.message(matchers=[is_human_direct_message])(direct_message_callback)
