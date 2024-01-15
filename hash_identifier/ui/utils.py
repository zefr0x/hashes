"""Usefull functions used in the UI."""
from typing import Callable

import gi

gi.require_version("Gdk", "4.0")
from gi.repository import Gdk  # noqa: E402


def clipboard_clauser(text: str) -> Callable:
    """Save a text to be used in a clipboard setter as handler funtion."""

    def handler(*args, **kargs) -> None:
        """Clipboard setter."""
        try:
            Gdk.Display.get_default().get_clipboard().set(text)  # type: ignore
        except AttributeError as e:
            print(e)

    return handler
