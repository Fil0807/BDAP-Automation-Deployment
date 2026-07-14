from setuptools import setup

APP = ["bdap_app/__main__.py"]

OPTIONS = {
    # Configurazione generale
    "argv_emulation": False,

    # Pacchetti da includere
    "packages": [
        "openpyxl",
        "matplotlib",
        "tkinterdnd2",
        "PIL",
    ],

    # Risorse del progetto
    "resources": [
        "Template_Analisi.xlsx",
        "image",
    ],

    # Informazioni dell'applicazione
    "plist": {
        "CFBundleName": "BDAP Automation",
        "CFBundleDisplayName": "BDAP Automation",
        "CFBundleIdentifier": "it.bdap.automation",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
    },

    # Compressione del pacchetto
    "compressed": True,

    # Ottimizzazione
    "optimize": 2,

    # Esclude librerie inutili
    "excludes": [
        "pytest",
        "tkinter.test",
        "unittest",
    ],
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)