i18n = import('i18n')

# Desktop file
desktop_file = i18n.merge_file(
  input: '@0@.desktop.in'.format(APP_ID),
  output: '@0@.desktop'.format(APP_ID),
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: datadir / 'applications'
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

# Appstream file
appstream_file = i18n.merge_file(
  input: '@0@.metainfo.xml.in'.format(APP_ID),
  output: '@0@.metainfo.xml'.format(APP_ID),
  po_dir: '../po',
  install: true,
  install_dir: datadir / 'metainfo'
)

appstream_util = find_program(['appstreamcli', 'appstreamcli'], required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', '--no-net', '--explain', appstream_file]
  )
endif

# Other meson.build sub files
subdir('icons/')
