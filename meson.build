project(
  'hashes',
  version : '1.0.0',
  license : 'GPL3',
  default_options : ['warning_level=2'],
)

APP_ID = 'io.github.zefr0x.hashes'
APP_BIN = 'hashes'
APP_VERSION = '1.0.0'

# Get options
prefix = get_option('prefix')
datadir = prefix / get_option('datadir')
bindir = prefix / get_option('bindir')
libdir = prefix / get_option('libdir')
localedir = prefix / get_option('localedir')

# Imports
gnome = import('gnome')

# Check for deps
gtk4 = dependency('gtk4', version: '>= 4.0')
# TODO: Consider libadwaita required version after completing the project.
libadwaita = dependency('libadwaita-1', version: '>= 1.4')

# Post install
gnome.post_install(
  gtk_update_icon_cache: true,
  update_desktop_database: true,
)

# Other meson.build sub files
subdir('data/')
subdir('po/')
subdir('hashes/')
