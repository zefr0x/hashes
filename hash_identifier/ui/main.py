"""Main file for the GUI."""
from typing import Sequence

import gi

from .main_window import HashIdentifierWindow
from hash_identifier.__about__ import APP_ID
from hash_identifier.__about__ import APP_NAME

gi.require_version("Adw", "1")
from gi.repository import Adw  # noqa: E402
from gi.repository import GLib  # noqa: E402


class HashIdentifier(Adw.Application):
    """The Main application class."""

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(application_id=APP_ID)
        GLib.set_application_name(APP_NAME)

    def do_activate(self) -> None:
        """Handle activate event."""
        Adw.Application.do_activate(self)

        self.window = self.props.active_window

        if not self.window:
            self.window = HashIdentifierWindow(self)

        self.window.present()


def main_ui(argv: Sequence[str]) -> int:
    """Launch the UI with arguments."""
    app = HashIdentifier()
    return app.run(list(argv))
