"""Usefull functions used in the UI."""

import logging
from typing import Callable

import gi

gi.require_version("Gdk", "4.0")
from gi.repository import Gdk  # noqa: E402


def clipboard_clauser(text: str) -> Callable:
    """Save a text to be used in a clipboard setter as handler funtion."""

    def handler(*_args: list, **_kargs: dict) -> None:
        """Clipboard setter."""
        try:
            Gdk.Display.get_default().get_clipboard().set(text)  # type: ignore[union-attr]
        except AttributeError:
            logging.exception("Error: Can't find GDK display to access clipboard.")

    return handler
