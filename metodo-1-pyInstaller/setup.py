from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from setuptools import Command, find_packages, setup

ROOT = Path(__file__).resolve().parent
DIST_DIR = ROOT / "dist"
BUILD_DIR = ROOT / "build" / "pyinstaller"

"""
DIST_DIR: Path della cartella di destinazione per l'eseguibile e le dipendenze.

BUILD_DIR: Path della cartella di lavoro temporanea per PyInstaller.
"""


class BuildExeCommand(Command):
    """
    Crea un eseguibile GUI per Windows con PyInstaller.

    Utilizzo:
        python setup.py build_exe

    Viene generata una cartella in dist/ contenente l'eseguibile e tutte
    le dipendenze, mantenendo invariato il comportamento dell'applicazione.
    """

    description = "Crea un eseguibile GUI per Windows con PyInstaller"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        cmd = [
            sys.executable,
            "-m",
            "PyInstaller",

            "--noconfirm",
            "--clean",
            "--windowed",
            "--onedir",

            "--name", "BDAP_Automation",

            "--distpath", str(DIST_DIR),
            "--workpath", str(BUILD_DIR),
            "--specpath", str(BUILD_DIR),

            "--hidden-import", "tkinterdnd2",
            "--hidden-import", "tkinterdnd2.TkinterDnD",

            "--add-data",
            f"{ROOT / 'Template_Analisi.xlsx'};.",

            str(ROOT / "bdap_app" / "__main__.py"),
        ]
        subprocess.check_call(cmd)

        print(f"\nExecutable output: {DIST_DIR / 'BDAP_Automation' / 'BDAP_Automation.exe'}")
        print(f"Dependency folder: {DIST_DIR / 'BDAP_Automation'}")


setup(
    name="bdap-automation",
    version="1.0.0",
    description="Automazione BDAP per la compilazione dei template Excel",
    packages=find_packages(include=["bdap_app", "bdap_app.*"]),
    cmdclass={
        "build_exe": BuildExeCommand,
    },
)
