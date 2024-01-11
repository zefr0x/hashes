#!@PYTHON@
"""A launcher for the application."""
import gettext
import locale
import sys

APP_ID = "@APP_ID@"
PKG_DATA_DIR = "@pkgdatadir@"
LOCALE_DIR = "@localedir@"

sys.path.insert(1, PKG_DATA_DIR)

locale.bindtextdomain(APP_ID, LOCALE_DIR)
locale.textdomain(APP_ID)
gettext.bindtextdomain(APP_ID, LOCALE_DIR)
gettext.textdomain(APP_ID)


def main() -> int:
    """Entry point for the application."""
    from hash_identifier.ui.main import main_ui

    main_ui(sys.argv)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
