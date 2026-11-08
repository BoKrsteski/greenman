# Greenman

have you ever had a directory full of random, unorganized stuff? No more!

Introducing Greenman, the ultimate directory organization tool!

## Versions:

### Greenman CLI

Greenman's initial version was a CLI application that could be run anywhere by being implemented into the unix PATH. It is still up to date and just as good, if not faster due to it's lightweightness than any other versions.
You can download it from the `greenman_for_cli` folder in the `main` branch. The initial version is only intended for unix based OSs and the PATH implementation has not been automated yet. that's coming soon!

### Greenman GUI 
coming soon!

## Commands:

NOTE: order of arguments does not matter!

### `organize` / `o`:

### usecase:

`o` is one of the core function of Greenman. It organizes any linked directory by your preferred criteria.

### arguments:

#### `-p` / `--path`:

the path to the directory you want organized. default is the current one.

example:

`greenman o -p path/to/my/stuff`

this will organize the `stuff` directory.

#### `-o` / `--only`:

this filters for extensions that you want organized. Default is all. Only want python files organized? Use `-o .py`

example:

`greenman o -o .py,.txt,.json`

this will only organize all python, text and json files in your current directory

### examples:

 `greenman o -p ~/home/user/Downloads` - organizes all files in the downloads directory

 `greenman o -p ~/home/user/Downloads -o .deb` - only organizes debian packages in your downloads

 `greenman o` - organizes all files in the current directory


### `unwrap` / `u`:

### usecase:

`u` is the direct counterpart to `o`. it unwraps any directories in the linked directory to extract all files from further diretories back into it.

### arguments:

#### `-p` / `--path`:

the path to the directory you want unwrapped. default is the current one.

example:

`greenman u -p path/to/my/stuff`

this will unwrap the `stuff` directory.

#### `-o` / `--only`:

this filters for extensions that you want unwrapped. Default is all. Only want python files unwrapped? Use `-o .py`

example:

`greenman u -o .py,.txt,.json`

this will only unwrap all python, text and json files in your current directory

#### `-d` / `--deep`:

use `-d` to also unwrap any directories following the first ones in your target directory. If you want the contents of `/one/two/three` back in `/one`, use `-d`. Otherwhise only the contents from `/one/two` will be moved to `/one` and the contents of `one/two/three` will remain there. -d works infinitely.

example:

`greenman u -d`

this will unwrap all contents off all following directories into this one. 

#### `-k` / `--known`:

`-k` will only unwrap known directories, meaning directories that have matching greenman names. So if you want to only revert organization changes made by greenman, use `-k`.

example:

`greenman u -k`

let's say you have 3 directories in your target: `text_files`,`crazyStuff3000` and `debian_packages`. `-k` will make it so that greenman will only unpack directories which it recognizes. Essentially greenman asks itself: "would I name a directory this way?". If so, it gets unwrapped. Otherwise it will be ignored. So in this situation, only `text_files` and `debian_packages` will be unwrapped.

