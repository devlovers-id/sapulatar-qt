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

- Python 3.8 (Rekomendasi 3.8.7) - [Download here](https://www.python.org/downloads/release/python-387/). Pastikan untuk mencentang opsi "Add to Path" ketika proses pemasangan.
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

Installer package in not available yet for now. But you can try to test Sapulatar-qt by following this steps.

### Linux

Open your terminal and run this command:
```bash
git clone https://github.com/devlovers-id/sapulatar-qt.git /tmp/sapulatar-qt
cd /tmp/sapulatar-qt
sudo python3 setup.py install
```

### Windows

Installer for windows is not available yet. If you wanna test on Windows, make sure yo've install all dependencies mentioned before. Then download the [source code here.](https://github.com/devlovers-id/sapulatar-qt/archive/refs/heads/master.zip) then extract it.

Open console window/cmd (Windows button + R then type cmd)
```bash
# Go to your extract folder
chdir C:\path\to\extracted\zip

sudo python3 setup.py install
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
