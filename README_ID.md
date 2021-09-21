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

Berkas paket instalasi memang belum tersedia, namun Anda dapat mencoba untuk menguji Sapulatar-qt dengan cara di bawah ini.

### Linux
```bash
curl -o- https://raw.githubusercontent.com/devlovers-id/sapulatar-qt/master/install.sh | bash
```

### Windows

Installer belum tersedia. Jika ingin mencoba di Windows, silakan lengkapi terlebih dahulu dependensi yang telah disebutkan di atas. Kemudian unduh kode sumber [di sini](https://github.com/devlovers-id/sapulatar-qt/archive/refs/heads/master.zip). 

Ekstrak hasil unduhan tersebut lalu klik ganda main.py. Jika ingin menjalakan Sapulatar-qt tanpa membuka jendela console, cukup rename `main.py` menjadi `sapulatar-qt.pyw`.

## Menemukan Bug?

Aplikasi stabil itu mitos. Jadi, jika Anda menemukan kutu atau mengalami kendala fatal saat menggunakan Sapulatar, silakan buat tiket laporan melalui Github Issue: https://github.com/devlovers-id/sapulatar-qt/issues. Kami akan mencoba untuk membantu mengatasi sebisa mungkin.

## Merasa Terbantu dengan Proyek ini?

Kami senang dapat membantu Anda memanfaatkan waktu serta menyelesaikan pekerjaan secara efisien. Jika Anda merasakan hal serupa, selain berdonasi, Anda dapat membentu pengembang misalnya dengan membuat tutorial, membuat ulasan, atau berbgai ke sekitar Anda tentang proyek ini. Hal tersebut akan menjadikan Anda, The Devlovers!

[Donate Now](https://support.dev-is.my.id)
**Tautan-Tautan**

- [Rembg repository](https://github.com/danielgatis/rembg)
- [Devlovers ID](https://dev-is.my.id)
