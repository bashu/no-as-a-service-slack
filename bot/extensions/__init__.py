import importlib
import pkgutil

from slack_bolt.app.async_app import AsyncApp


def register_extensions(app: AsyncApp) -> None:
    """Import every subpackage of bot/extensions and call its register(app)."""
    for module in pkgutil.iter_modules(__path__, f"{__name__}."):
        importlib.import_module(module.name).register(app)
