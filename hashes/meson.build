pkgdatadir = libdir / APP_ID
main_moduledir = pkgdatadir / 'hashes'

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('APP_ID', APP_ID)
conf.set('APP_VERSION', APP_VERSION)
conf.set('localedir', prefix / localedir)
conf.set('pkgdatadir', pkgdatadir)

python_installation = python.find_installation(
  'python3',
  required : true,
  modules : [
    'gi',  # PyGObject
    'name_that_hash',  # name-that-hash
  ]
)

configure_file(
  input: '__main__.py',
  output: APP_BIN,
  configuration: conf,
  install: true,
  install_dir: bindir,
  install_mode: ['rwxr-xr-x']
)

sources = [
  '__init__.py',
  configure_file(input: '__about__.py', output: '__about__.py', configuration: conf)
]

install_data(sources, install_dir: main_moduledir)

# Other meson.build sub files
subdir('ui/')
