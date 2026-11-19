#!/usr/bin/env bash
ln -sf "$(dirname "$0")/CLIgreenman.py" ~/bin/greenman
chmod +x CLIgreenman.py
greenman v
read -p "Press Enter to exit..."