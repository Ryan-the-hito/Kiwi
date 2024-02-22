# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

__version__ = '1.0.1'

info_plist = {
    'LSUIElement': True,
    #'LSBackgroundOnly': True,
}

a = Analysis(
    ['KiwiAuto.py'],
    pathex=['/Users/ryanshenefield/Downloads/KiwiAuto.py'],
    binaries=[],
    datas=[('kiwi-dsk.icns', '.'), ('kiwi-logo.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KiwiAuto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='KiwiAuto',
)
app = BUNDLE(
    coll,
    name='KiwiAuto.app',
    icon='kiwi-dsk.icns',
    info_plist=info_plist,
    bundle_identifier=None,
    version=__version__,
)
