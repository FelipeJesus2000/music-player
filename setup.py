import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"], 
    "includes": ["tkinter",
        "pathlib",
        "time",
        "Tapes.Tapes",
        "pygame",
        "json"
    ]
    }
build_exe_options = dict(include_files = [('img', 'lib/img'), 
                                     ('albums', 'lib/albums')
                                     ],
                    packages = ["tkinter","time","pathlib","pygame","json"],
                    includes = [
                        "Tapes.Tapes",
                        "NewTape.NewTape",
                        "img"
                    ],  ## Include the modules here
                    optimize = 2,
                    )

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Toca fitas",
    version="0.1",
    description="Um tocador de fitas, escolha uma das fitas do json e se divirta!!!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)