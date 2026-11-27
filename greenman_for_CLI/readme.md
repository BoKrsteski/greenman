# TODO Make .sh executable from both os specific and gen dir 


# Greenman for CLI!

here you can get the necessary files to connect GreenmanCLI to your PATH. 

__Documentation for OS specific installs is below__

# how to install:

First, get `greenmancore.py` and `CLIgreenman.py` from this directory and put them in the same (preferrably new) directory.

Then, go on to downloading your OS specific PATHbinder.

__They are found in the `OS_specific` folder__

# which version to choose:

choose the version that matches your OS. The linux version is compatible with most unix systems.

# Greenman CLI windows version
## set up:

First, install both python files from this directory 

then, install `WINDOWS_greenman-PATHbinder.bat` from the __OS_specific__ folder.

Now, to set up Greenman CLI in your windows terminal, ensure that `WINDOWS_greenman-PATHbinder.bat`, as well as `CLIgreenman.py` have execution permissions.

(Although `greenmancore.py` is extremely important. It doesn't need any permissions, as it gets imported by `CLIgreenman.py`)

Make sure all files are in the same directory (preferably even in their very own one). then execute `WINDOWS_greenman-PATHbinder.bat`

After you've done that, check if greenman works by typing any greenman command (e.g. `greenman v --init`) in your CLI. This should now work in any directory.

That's the PATH magic for ya :)

# Greenman CLI linux (unix) version

## set up:

First, install both python files from this directory 

then, get the `LINUX_greenman-PATHbinder.sh` file from the __OS_specific__ folder.

Now, to set up Greenman CLI in your linux terminal, ensure that `LINUX_greenman-PATHbinder.sh` has the `+x` permission. They should have it by default but you never know.

If they don't have the `+x` permission, run `chmod +x LINUX_greenman-PATHbinder.sh CLIgreenman.py`. Now they should have it.

(Although `greenmancore.py` is extremely important. It doesnt need any permissions, as it gets imported by `CLIgreenman.py`)

Make sure all files are in the same directory (preferably even in their very own one). then execute `LINUX_greenman-PATHbinder.sh`.

Usually this doesn't require superuser rights.

After you've done that, check if greenman works by typing any greenman command (e.g. `greenman v --init`) in your CLI. This should now work in any directory. 

That's the PATH magic for ya :)
