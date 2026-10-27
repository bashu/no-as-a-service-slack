from slack_bolt.app.async_app import AsyncApp

from bot import blocks

from .no_preview import cancel_callback, send_callback, shuffle_callback


def register(app: AsyncApp) -> None:
    app.action(blocks.SEND_ACTION_ID)(send_callback)
    app.action(blocks.SHUFFLE_ACTION_ID)(shuffle_callback)
    app.action(blocks.CANCEL_ACTION_ID)(cancel_callback)
