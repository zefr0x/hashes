"""Main file for the GUI."""

import contextlib
from typing import Sequence

import gi

from hashes.__about__ import APP_ID, APP_NAME

from .main_window import HashesMainWindow

gi.require_version("Adw", "1")
from gi.repository import (  # noqa: E402
    Adw,
    Gio,
    GLib,
)


class Hashes(Adw.Application):
    """The Main application class."""

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(
            application_id=APP_ID,
            flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
        )
        GLib.set_application_name(APP_NAME)

        # Setup CLI options
        # TODO: Consider localizing CLI options.
        self.add_main_option(
            "hash",
            0,
            GLib.OptionFlags.NONE,
            GLib.OptionArg.STRING,
            "Hash to identify",
            None,
        )

    def do_command_line(self, command_line: Gio.ApplicationCommandLine) -> int:
        """Handle CLI args."""
        self.argv = command_line.get_options_dict().end().unpack()

        self.activate()

        return 0

    def do_activate(self) -> None:
        """Handle activate event."""
        Adw.Application.do_activate(self)

        self.window = self.props.active_window

        if not self.window:
            self.window = HashesMainWindow(self)

        self.window.present()

        # Pass CLI args to the main window
        with contextlib.suppress(AttributeError, KeyError):
            self.window.identify_hash(self.argv["hash"])  # type: ignore[attr-defined]


def main_ui(argv: Sequence[str]) -> int:
    """Launch the UI with arguments."""
    app = Hashes()
    return app.run(list(argv))
