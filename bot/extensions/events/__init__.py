from slack_bolt.app.async_app import AsyncApp

from .app_mention import app_mention_callback


def register(app: AsyncApp) -> None:
    app.event("app_mention")(app_mention_callback)
    # Delete a workspace's stored tokens when it uninstalls the app or revokes them
    app.enable_token_revocation_listeners()
