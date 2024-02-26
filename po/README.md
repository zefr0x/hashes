You can use [Gtranslator](https://flathub.org/apps/org.gnome.Gtranslator) or [Lokalize](https://apps.kde.org/lokalize/) to edit `.po` files.

## Adding New Language

1. Find you language's locale code.

> Locale codes are typically of the form language[_territory], where language is an [ISO 639 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), territory is an [ISO 3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes).
>
> Source: https://wiki.archlinux.org/title/locale#Generating_locales

2. Copy [`io.github.zefr0x.hashes.pot`](io.github.zefr0x.hashes.pot) to `<LOCALE CODE>.po`
3. Add the locale code to the [`LINGUAS`](LINGUAS) file in an alphabetical order.

## Management Using Meson

### Generate the `.pot` file

Run the `io.github.zefr0x.hashes-pot` compile target.

### Update `.po` files from current `.pot` file

Run the `io.github.zefr0x.hashes-update-po` compile target.
