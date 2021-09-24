# Sapulatar-qt

Perkakas GUI ringkas untuk membantu Anda menghapus latar pada gambar/foto. Perkakas ini membutuhkan modul Rembg untuk memproses gambar Anda. Pastikan modul tersebut telah terpasang di sistem kecuali Anda menggunakan sapulatar sebagai klien pada jaringan internal. 

## Dependencies

### Linux

- Python3 (Minimal Python 3.8)
- rembg
    ```bash
    python3 -m pip install rembg
    
    # Jalankan pertama untuk memasang data model
    rembg --help
    rembg input.jpg -o output.jpg
    ```
- PySide2
    ```bash
    python3 -m pip install PySide2
    ```

### Windows

> Aplikasi ini bukan untuk yang ogah repot, karena untuk memasang di Windows prosesnya agak panjang.

- Python 3.8 (Rekomendasi 3.8.7) - [Unduh di sini](https://www.python.org/downloads/release/python-387/). Pastikan untuk mencentang opsi "Add to Path" ketika proses pemasangan.
- Ms Visualstudio C++ build tools - [Unduh di sini](https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe)
- rembg
    ```bash
    python3 -m pip install rembg

    # Jalankan pertama untuk memasang data model
    rembg --help
    rembg input.jpg -o output.jpg
    ```
- PySide2
    ```bash
    python3 -m pip install PySide2
    ```

## Install

Anda dapat memasang Sapulatar melalui kanal [Pypi](https://pypi.org/project/sapulatar-qt/) dengan menjalankan perintah berikut:

```bash
pip install sapulatar-qt

atau

python3 -m pip install sapulatar-qt
```

For uninstall, just run: 

```bash
pip uninstall sapulatar-qt

atau

python3 -m pip uninstall sapulatar-qt
```


## Menemukan Bug?

Aplikasi stabil itu mitos. Jadi, jika Anda menemukan kutu atau mengalami kendala fatal saat menggunakan Sapulatar, silakan buat tiket laporan melalui Github Issue: https://github.com/devlovers-id/sapulatar-qt/issues. Kami akan mencoba untuk membantu mengatasi sebisa mungkin.

## Merasa Terbantu dengan Proyek ini?

Kami senang dapat membantu Anda memanfaatkan waktu serta menyelesaikan pekerjaan secara efisien. Jika Anda merasakan hal serupa, selain berdonasi, Anda dapat membentu pengembang misalnya dengan membuat tutorial, membuat ulasan, atau berbgai ke sekitar Anda tentang proyek ini. Hal tersebut akan menjadikan Anda, The Devlovers!

[Donate Now](https://support.dev-is.my.id)
**Tautan-Tautan**

- [Rembg repository](https://github.com/danielgatis/rembg)
- [Devlovers ID](https://dev-is.my.id)
