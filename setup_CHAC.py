import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    # "packages": ["main"],
}
setup(
    name="CHAC",
    version="0.1.1",
    description="CHild At the Computer",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('main.py',
                            base='Win32GUI',
                            targetName='CHAC.exe',
                            )]
)