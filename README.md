<div align = center>

![Logo](data/icons/io.github.zefr0x.hashes.svg)

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

<a href='https://flathub.org/apps/io.github.zefr0x.hashes'>
    <img width='240' alt='Download on Flathub' src='https://flathub.org/api/badge?locale=en'/>
</a>

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

![Screenshot Light Theme](https://github.com/zefr0x/hashes/assets/65136727/f54f186b-4384-41dd-b4a5-205c198b43d4)
![Screenshot Dark Theme](https://github.com/zefr0x/hashes/assets/65136727/3ee65148-b8a0-4f39-8023-06a005c07034)
![Screenshot Small Light Theme](https://github.com/zefr0x/hashes/assets/65136727/1506f222-cafa-4d9e-91d8-c72ea536f541)
![Screenshot Small Dark Theme](https://github.com/zefr0x/hashes/assets/65136727/deec13ca-9246-4b99-8762-1c93a532a979)

## Acknowledgments

- **[Name-That-Hash](https://github.com/HashPals/Name-That-Hash)** - For providing an API first and modern hash identification system.
- **[Bottles](https://github.com/bottlesdevs/Bottles)** - For showing how to deal with a python project using [Meson](https://mesonbuild.com/).
- **[Dialect](https://github.com/dialect-app/dialect)** - For showing how to deal with CLI in python PyGObject application.
