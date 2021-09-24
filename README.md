# sapulatar-qt

A simple gui apps to help you remove background from various images. This tool need Rembg module to done its job. Please install it first if the module not exist yet in your system. 

## Dependencies

### Linux

- Python3 (Minimal Python 3.8)
- rembg
    ```bash
    python3 -m pip install rembg
    
    # At first time, run some commands in order to dowload data model
    rembg --help
    rembg input.jpg -o output.jpg
    ```
- PySide2
    ```bash
    python3 -m pip install PySide2
    ```

### Windows
> Some dependencies need more space of storage, dwyor.

- Python 3.8 (3.8.7 is recomended) - [Download here](https://www.python.org/downloads/release/python-387/). Make sure you've check "Add to Path" option when installing.
- Ms Visualstudio C++ build tools - [Download here](https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe)
- rembg
    ```bash
    python3 -m pip install rembg

    # At first time, run some commands in order to dowload data model
    rembg --help
    rembg input.jpg -o output.jpg
    ```
- PySide2
    ```bash
    python3 -m pip install PySide2
    ```

## Install

You can install sapulatar-qt via [Pypi](https://pypi.org/project/sapulatar-qt/) by running this command:

```bash
pip install sapulatar-qt

or 

python3 -m pip install sapulatar-qt
```

For uninstall, just run: 

```bash
pip uninstall sapulatar-qt

or 

python3 -m pip uninstall sapulatar-qt
```

## Found A Bug?

Stability is a myth. So, if you find a bug or get a crash while using Sapulatar, please report it via Github Issue: https://github.com/devlovers-id/sapulatar-qt/issues
We'll check it as soon as we can and provide regular updates.

## Feel Helpful with this Project?

We're happy to save you time and help get your task done efficiently. If you feel the same, besides donating, you can help the developer by making tutorials, reviews, or the like for other people to know about this project. It will make you, the Devlovers!
[Donate Now](https://support.dev-is.my.id)

**Usefull link**

- [Rembg repository](https://github.com/danielgatis/rembg)
- [Devlovers ID](https://dev-is.my.id)
