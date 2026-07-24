# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files


# File aggiuntivi da includere
datas = [
    ("Template_Analisi.xlsx", "."),
]

# Dati necessari a matplotlib
datas += collect_data_files("matplotlib")


# Hidden imports
hiddenimports = [
    "PIL.Image",
    "PIL.ImageTk",
    "matplotlib.backends.backend_tkagg",
]


# Moduli da escludere
excludedimports = [
    "PIL._avif",
]


# Analisi
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


# Archivio Python
pyz = PYZ(a.pure)


# Eseguibile
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="BDAP Automation",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
)


# Bundle macOS
app = BUNDLE(
    exe,
    name="BDAP Automation.app",
    bundle_identifier="it.bdap.automation",

    # sostituire con "icon.icns" quando disponibile
    icon=None,
)
