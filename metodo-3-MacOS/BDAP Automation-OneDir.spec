# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

# File da includere nel bundle
datas = [
    ("Template_Analisi.xlsx", "."),
]

# Dati necessari a matplotlib
datas += collect_data_files("matplotlib")

# Import che PyInstaller potrebbe non rilevare automaticamente
hiddenimports = [
    "PIL.Image",
    "PIL.ImageTk",
    "matplotlib.backends.backend_tkagg",
]

# Moduli da escludere
excludedimports = [
    "PIL._avif",
]

a = Analysis(
    ["bdap_app/__main__.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludedimports,
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="BDAP Automation",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name="BDAP Automation",
)

app = BUNDLE(
    coll,
    name="BDAP Automation.app",
    bundle_identifier="it.bdap.automation",
)
