# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

__version__ = '0.0.3'

a = Analysis(
    ['Kiwi.py'],
    pathex=['/Users/ryanshenefield/Downloads/Kiwi.py'],
    binaries=[],
    datas=[('kiwi-logo.icns', '.'), ('kiwi-dsk.icns', '.'), ('kiwi-logo.png', '.'), ('wechat50.png', '.'), ('wechat20.png', '.'), ('wechat10.png', '.'), ('wechat5.png', '.'), ('alipay50.png', '.'), ('alipay20.png', '.'), ('alipay10.png', '.'), ('alipay5.png', '.'), ('RestTime.txt', '.'), ('SetTime.txt', '.'), ('ReLa.txt', '.'), ('green.gif', '.'), ('DockVi.txt', '.'), ('menu_height.txt', '.'), ('DockRe.txt', '.'), ('cosine_plot0.png', '.')],
    hiddenimports=['subprocess', 'AppKit'],
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
    name='Kiwi',
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
    name='Kiwi',
)
app = BUNDLE(
    coll,
    name='Kiwi.app',
    icon='kiwi-dsk.icns',
    bundle_identifier=None,
    version=__version__,
)
