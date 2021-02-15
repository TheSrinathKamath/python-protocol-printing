from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="PP20",
    options=options,
    version="1.0.0",
    description='Direct print manager',
    executables=executables
)
