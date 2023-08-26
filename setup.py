from pathlib import Path
from distutils.core import setup


req_file = Path(__file__).resolve().parent / "requirements.txt"
with open(req_file, "r") as f:
    reqs = f.read().splitlines()

setup(
    name="app",
    version="1.0",
    py_modules=['app'],
    install_requires=reqs
)
