import sys,os
from cx_Freeze import setup,Executable

files=['menu','models','processes','windows','reportes','templates','windows']

exe=Executable(script="app.py",base="Win32GUI")


setup(
    name="America",
    version="1.0",
    description="algo",
    author="Vladimir Marcos",
    options={'buil_exe':{'include_files':files}},
    executables=[exe]
)