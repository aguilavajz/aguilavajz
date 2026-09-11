#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -f "venv/bin/activate" ]; then
  echo "Error: Python virtual environment not found at venv/bin/activate." >&2
  echo "Create it with: python3 -m venv venv" >&2
  exit 1
fi
source venv/bin/activate
python3 send_invites.py
