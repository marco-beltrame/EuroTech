import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "tkinter", "ctypes", "matplotlib", "pandas"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "EuroTech Data Analyzer",
    version = "0.1",
    description = "Analizzatore di dati per i dati provenienti dalla centralina Eurotech dell'istituto A. Malignani, Udine.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("App.py", base=base, icon="icon.ico")]
)