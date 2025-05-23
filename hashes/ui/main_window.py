"""Main application window."""

import logging
from gettext import gettext as _
from typing import Callable

import gi
from name_that_hash.runner import api_return_hashes_as_dict

from hashes.__about__ import (
    APP_ARTISTS_LIST,
    APP_AUTHOR,
    APP_DEVELOPERS_LIST,
    APP_ID,
    APP_VERSION,
    BUG_REPORT_URL,
    PROJECT_HOME_PAGE_URL,
)

gi.require_version("Adw", "1")
gi.require_version("Gtk", "4.0")
from gi.repository import (  # noqa: E402
    Adw,
    Gdk,
    Gtk,
)

logger = logging.getLogger(__name__)


class HashesMainWindow(Adw.ApplicationWindow):
    """Main window."""

    def __init__(self, application: Adw.Application) -> None:
        """Initialize main window."""
        super().__init__(
            application=application,
            title=_("Hashes"),
            default_width=500,
            default_height=800,
        )

        # Main layout
        main_layout = Adw.ToolbarView()
        self.set_content(main_layout)

        # Window header
        main_layout.add_top_bar(self.__build_header())

        # Content layout
        main_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Hash input filed
        self._hash_input_field = Gtk.Entry(
            primary_icon_name="dialog-password-symbolic",
            placeholder_text=_("Enter a hash text"),
            margin_start=12,
            margin_end=12,
            margin_top=6,
            margin_bottom=6,
        )
        main_layout.add_top_bar(self._hash_input_field)
        self._hash_input_field.connect("changed", self.__hash_input_changed)
        # Move focus to the input when window first opened
        self._hash_input_field.grab_focus()

        # TODO: Add option to show only popular algorithmes.
        # TODO: Add option to handle base64 input text.

        # Results body placeholders
        self._no_input_placeholder = Gtk.Label(label=_("Waiting for input…"))
        self._no_results_placeholder = Gtk.Label(
            label=_("Can't find an algorithm that matches your input!")
        )

        # Body scrollable bin
        self._body_bin = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        main_content.append(self._body_bin)

        self._body_bin.set_child(self._no_input_placeholder)

        # Main Overlay
        self._overlay = Adw.ToastOverlay(child=main_content)
        main_layout.set_content(self._overlay)

        # Main Overlay's Toasts
        self._toast_copied = Adw.Toast(title=_("Copied"), timeout=2)

    def __build_header(self) -> Adw.HeaderBar:
        """Create the header bar for the application."""
        header = Adw.HeaderBar()

        # About applicaiton button
        about_button = Gtk.Button(icon_name="help-about-symbolic")
        header.pack_end(about_button)
        about_button.connect("clicked", self.__show_about_dialog)

        return header

    def identify_hash(self, hash_text: str) -> None:
        """
        Write text to the input field.

        Used to pass input from the CLI.
        """
        self._hash_input_field.set_text(hash_text)

    def __hash_input_changed(self, entry: Gtk.Entry) -> None:
        """Handle hash input entry change event."""
        input_text = entry.get_text()
        hash_results = api_return_hashes_as_dict([input_text], {"popular_only": False})[
            input_text
        ]

        if len(hash_results):
            # Colorize entry with to green color
            entry.set_css_classes(("success",))

            # This layout contain one or more result frames
            results_layout = Gtk.FlowBox(
                orientation=Gtk.Orientation.HORIZONTAL,
                margin_start=40,
                margin_end=40,
                margin_top=20,
                margin_bottom=20,
                row_spacing=5,
                column_spacing=5,
                selection_mode=Gtk.SelectionMode.NONE,
                activate_on_single_click=False,
                valign=Gtk.Align.START,
            )
            self._body_bin.set_child(results_layout)

            for result in hash_results:
                results_layout.append(self.__build_result_box(result))
        elif input_text:
            # When there is input but there is not results

            # Colorize entry with red color
            entry.set_css_classes(("error",))

            self._body_bin.set_child(self._no_results_placeholder)
        else:
            # When there is no input or results

            # Reset entry color
            entry.remove_css_class("success")
            entry.remove_css_class("error")

            self._body_bin.set_child(self._no_input_placeholder)

    def __build_result_box(self, result: dict) -> Gtk.Frame:
        """Create a frame for a result."""
        # TODO: Color results based on popularity?
        result_flags_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            halign=Gtk.Align.START,
            margin_start=5,
            margin_end=5,
            margin_bottom=5,
            spacing=5,
        )

        if result["extended"]:
            result_flags_box.append(
                Gtk.Image(
                    icon_name="emblem-important-symbolic",
                    tooltip_markup=_("<b>Extended!</b>"),
                    margin_start=5,
                )
            )

        if result["hashcat"]:
            hashcat_id = str(result["hashcat"])

            button = Gtk.Button(
                child=Adw.ButtonContent(
                    icon_name="edit-copy-symbolic",
                    label=_("Hashcat"),
                    tooltip_text=hashcat_id,
                ),
                css_classes=("flat",),
            )
            result_flags_box.append(button)
            button.connect("clicked", self.__clipboard_clauser(hashcat_id))

        if result["john"]:
            john_id = str(result["john"])

            button = Gtk.Button(
                child=Adw.ButtonContent(
                    icon_name="edit-copy-symbolic",
                    label=_("John"),
                    tooltip_text=john_id,
                ),
                css_classes=("flat",),
            )
            result_flags_box.append(button)
            button.connect("clicked", self.__clipboard_clauser(john_id))

        return Gtk.Frame(
            label_widget=Gtk.Label(
                label=result["name"],
                # TODO: Handle URLs in the description.
                tooltip_markup=result["description"],
                css_classes=("title-3",),
            ),
            child=result_flags_box,
        )

    def __clipboard_clauser(self, text: str) -> Callable:
        """Save a text to be used in a clipboard setter as handler funtion."""

        def handler(*_args: list, **_kargs: dict) -> None:
            """Clipboard setter."""
            self._toast_copied.dismiss()

            try:
                Gdk.Display.get_default().get_clipboard().set(text)  # type: ignore[union-attr]
            except AttributeError:
                logger.exception("Error: Can't find GDK display to access clipboard.")
            else:
                self._overlay.add_toast(self._toast_copied)

        return handler

    def __show_about_dialog(self, _button: Gtk.Button) -> None:
        """Present the app's about dialog."""
        about_window = Adw.AboutDialog(
            application_icon=APP_ID,
            application_name=self.get_title() or "",
            developer_name=APP_AUTHOR,
            developers=APP_DEVELOPERS_LIST,
            artists=APP_ARTISTS_LIST,
            # TRANSLATORS: The string may contain email addresses and URLs.
            translator_credits=_("translator-credits"),
            copyright="© 2024 " + APP_AUTHOR,
            issue_url=BUG_REPORT_URL,
            license_type=Gtk.License.GPL_3_0_ONLY,
            version=APP_VERSION,
            website=PROJECT_HOME_PAGE_URL,
        )

        about_window.add_acknowledgement_section(
            _("External Libraries"),
            [
                "Name That Hash https://github.com/HashPals/Name-That-Hash",
                "PyGobject https://gitlab.gnome.org/GNOME/pygobject",
            ],
        )

        about_window.present(self)
