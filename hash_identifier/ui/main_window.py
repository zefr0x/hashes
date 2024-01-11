"""Main application window."""
from gettext import gettext as _

import gi

gi.require_version("Adw", "1")
gi.require_version("Gtk", "4.0")
from gi.repository import Adw  # noqa: E402
from gi.repository import Gtk  # noqa: E402


class HashIdentifierWindow(Adw.ApplicationWindow):
    """Main window."""

    def __init__(self, application: Adw.Application) -> None:
        """Initialize main window."""
        super().__init__(application=application, title=_("Hash Identifier"))

        self.set_application(application)

        main_layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(main_layout)

        header = Adw.HeaderBar()
        main_layout.append(header)
