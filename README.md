<div align = center>

<h1>Hashes</h1>

Simple hash algorithm identification [Linux](https://en.wikipedia.org/wiki/Linux) [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface).

---

[<kbd><br><b>Install</b><br><br></kbd>](#installation)
[<kbd><br><b>Screenshots</b><br><br></kbd>](#screenshots)
[<kbd><br><b>Contribute</b><br><br></kbd>](CONTRIBUTING.md)
[<kbd><br><b>Packaging</b><br><br></kbd>](PACKAGING.md)

---

<br>

</div>

## Features

- 📺 **Popularity Ratings** - Most popular hashes showed first.
- 👵 **Updated\!** - New hash algorithm database is used in the identification process.
- 🚫 Microsoft Windows is not supported.

## Requirements

- [GTK4](https://www.gtk.org/)
- [Adwaita](https://gitlab.gnome.org/GNOME/libadwaita/)

## Installation

### Flathub <sup>`(recomended)`</sup>

TODO...

### Git

> You need to have [`meson`](https://mesonbuild.com/) and [`xgettext`](https://www.gnu.org/software/gettext/) installed in you system.
>
> You need python modules listed in [`requirements/requirements.in`](requirements/requirements.in) installed in your python environment.

```shell
git clone https://github.com/zefr0x/hashes.git
cd hashes
meson setup builddir
meson install -C builddir
```

## Screenshots

TODO...

## Acknowledgments

- **[Name-That-Hash](https://github.com/HashPals/Name-That-Hash)** - For providing an API first and modern hash identification system.
- **[Bottles](https://github.com/bottlesdevs/Bottles)** - For showing how to deal with a python project using [Meson](https://mesonbuild.com/).
- **[Dialect](https://github.com/dialect-app/dialect)** - For showing how to deal with CLI in python PyGObject application.
