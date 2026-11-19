<p align="center">
  <img src="greenman_GUI/data/icons/greenman.png" width="120" alt="Greenman">
</p>

<h1 align="center">Greenman</h1>

<p align="center">
  Have you ever had a directory full of random, unorganized stuff? No more!<br><br>
  <b>Introducing Greenman</b> — the ultimate directory organization tool.
</p>

---

## Versions

<h3>Greenman CLI <img src="greenman_GUI/data/icons/CLIgreenman.png" width="48" align="absmiddle" alt="CLI"></h3>   

Greenman's initial version was a CLI application that could be run anywhere by being implemented into the unix PATH. It is still up to date and just as good, if not faster due to its lightweightness than any other versions.

You can download it from the [releases tab](https://github.com/YOUR_USER/YOUR_REPO/releases) or the `greenman_for_cli` folder in the `main` branch.

<h3>Greenman GUI <img src="greenman_GUI/data/icons/GUIgreenman.png" width="48" align="absmiddle" alt="GUI"></h3>

<p><b>In development now. Coming soon!</b></p>   

---

## How to install

You can directly download all files for the CLI version in the **releases** tab. Or you can only get the files you need from the folder in the source code. The readme will contain further instructions.

The GUI version will also be available in the **releases** tab as an executable.

---

## Greenman CLI Commands

> **NOTE:** order of arguments does not matter!

### `help`

**Use case:**
`help` is used to get help with certain commands or with greenman in general, though it is not yet very thorough. Additions will come soon. For now rely on the `README`.

**Arguments:**

`command` — `help` only takes one argument, so just type `help` followed by the command you want help with. Type `help list` to see a list of commands.

**Examples:**

```
greenman help              # receive general help
greenman help o            # receive help with the `o` command
greenman help list         # list of items you can get help with
```

---

### `organize` / `o`

**Use case:**
`o` is one of the core functions of Greenman. It organizes any linked directory by your preferred criteria.

**Arguments:**

| Flag | Description |
|------|-------------|
| `-p` / `--path` | Path to the directory to organize. Default: current. |
| `-o` / `--only` | Filter by extensions. Default: all. |

**Examples:**

```
greenman o -p ~/Downloads
greenman o -p ~/Downloads -o .deb
greenman o
```

---

### `unwrap` / `u`

**Use case:**
`u` is the direct counterpart to `o`. It unwraps any directories in the linked directory to extract all files back into the target.

**Arguments:**

| Flag | Description |
|------|-------------|
| `-p` / `--path` | Path to the directory to unwrap. Default: current. |
| `-o` / `--only` | Filter by extensions. Default: all. |
| `-d` / `--deep` | Recursively unwrap nested directories. |
| `-k` / `--known` | Only unwrap directories Greenman recognizes. |
| `-D` / `--onlydir` | Filter for specific directory names. |

**Examples:**

```
greenman u -d            # unwrap all nested contents into current dir
greenman u -k            # only unwrap Greenman-named directories
greenman u -D coolstuff  # only unwrap "coolstuff"
```

---

### `knownlist` / `klist` / `kl`

**Use case:**
`kl` displays all extensions and dirnames known to greenman. Useful if you want to see what `greenman u -k` includes.

**Arguments:** None lol

**Example:**

```
greenman kl
```   
