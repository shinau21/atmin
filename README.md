<p align="center"><img src="assets/img/logo.png" width="200"></p>


## ATMIN PYTHON

ATM Mini (ATMIN) Python ini digunakan selayaknya mesin ATM pada umumnya.

Fitur ATMIN:

- Multiple Akun ATMIN.
- 3 Jenis Saldo.
- 3 Opsi Tarik Uang.
- 3 Opsi Simpan Uang.
- Logging ke dalam file.

## Bahan

Code Editor : VSCode [[LINK]](https://code.visualstudio.com/download)

Python Version : 3.8 [[LINK]](https://www.python.org/downloads/release/python-386/)

MariaDB Version : 10.x [[LINK]](https://mariadb.com/downloads/)

## Setup

Install terlebih dahulu bahan diatas, lalu buka cmd / terminal, 

buat database dengan nama atmin, caranya

```bash
mysql -u user -p

CREATE DATABASE atmin;
exit

mysql -u user -p atmin < config/config.sql
```

default user mariadb = root</br>default root password =

sesuaikan koneksi user dan password database di customer.py sesuai dengan koneksi database anda.

kemudian install library pymysql dengan cara

```bash
python3 -m pip install pymysql
```

setelah itu jalankan atm_program.py

```bash
python3 atm_program.py
```

## Donasi Pengembangan

Dukung kami dengan cara donasi ke Rekening dibawah ini, donasi anda sangat bermanfaat untuk pengembangan kami selanjutnya
<p align="center">
DANA :</br>
    <img src="assets/img/dana.png" width="200"></img></br>
</br>
SocialBuzz :</br>
   <a href="https://sociabuzz.com/shinau21/donate" target="_blank"><img src="assets/img/socialbuzz.png" width="200"></img></a>

## Kontak
Untuk request project silahkan hubungi lewat WA : [RAFLI SETIAWAN](https://wa.me/6285702429294).

## Lisensi

ATMIN merupakan perangkat lunak bersumber terbuka yang dilisensikan di bawah [Lisensi MIT](https://opensource.org/licenses/MIT).