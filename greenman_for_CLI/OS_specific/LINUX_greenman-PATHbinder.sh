#!/usr/bin/env bash
ln -sf "$(dirname "$0")/CLIgreenman.py" ~/bin/greenman
chmod +x CLIgreenman.py
echo done! Greenman is all set up!
greenman help help
read -p "Press Enter to exit..."   