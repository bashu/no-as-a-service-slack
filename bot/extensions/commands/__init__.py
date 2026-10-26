from slack_bolt.app.async_app import AsyncApp

from .no import no_callback


def register(app: AsyncApp) -> None:
    app.command("/no")(no_callback)
