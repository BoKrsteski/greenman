# Greenman for CLI!

here you can get the necessary files to connect GreenmanCLI to your PATH. 

__Documentation for OS specific installs is below__

# how to install:

First, get `greenmancore.py` and `CLIgreenman.py` from this directory and put them in the same (preferrably new) directory

# which version to choose:

choose the version that matches your OS. The linux version is compatible with most unix systems.

# Greenman CLI windows version
## set up:

First, install all files in this directory (except for the README)

Now, to set up Greenman CLI in your windows terminal, ensure that installer.bat, as well as CLIgreenman.py have execution permissions.

(Although greenmancore.py is extremely important. It doesnt need any permissions, as it gets imported by CLIgreenman.py)

Make sure all files are in the same directory (preferably even in their very own one). then execute installer.bat

After you've done that, check if greenman works by typing any greenman command (e.g. greenman help help) in your CLI. This should now work in any directory.

That's the PATH magic for ya :)

# Greenman CLI linux (unix) version

## set up:

First, Download all the contents of this folder (except the README)

Now, to set up Greenman CLI in your linux terminal, ensure that `PATHbinder.sh`, as well as `CLIgreenman.py` have the `+x` permission. They should have it by default but you never know.

If they don't have the `+x` permission, run `chmod +x PATHbinder.sh CLIgreenman.py`. Now they should have it.

(Although `greenmancore.py` is extremely important. It doesnt need any permissions, as it gets imported by `CLIgreenman.py`)

Make sure all files are in the same directory (preferably even in their very own one). then execute `PATHbinder.sh`.

Usually this doesn't require superuser rights.

After you've done that, check if greenman works by typing any greenman command (e.g. `greenman help help`) in your CLI. This should now work in any directory. 

That's the PATH magic for ya :)
