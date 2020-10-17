<p align="center"><img src="assets/img/logo.png" width="200"></p>


## ATMIN PYTHON

ATM Mini (ATMIN) Python ini digunakan selayaknya mesin ATM pada umumnya.

Fitur ATMIN:

- 1 Akun ATMIN.
- 3 Jenis Saldo.
- 3 Opsi Tarik Uang.
- 3 Opsi Simpan Uang.
- Logging ke dalam file.

## Requirement

Code Editor : VSCode [[LINK]](https://code.visualstudio.com/download)

Python Version : 3.8 [[LINK]](https://www.python.org/downloads/release/python-386/)

MariaDB Version : 10.x

## Setup

Install terlebih dahulu requirement diatas, lalu buka cmd / terminal, 

buat database dengan nama atmin, caranya

```bash
mysql -u root -p

CREATE DATABASE atmin;
exit

mysql -u root -p atmin < config/config.sql
```


kemudian install library pymysql dengan cara

```bash
python3 -m pip install pymysql
```

setelah itu jalankan atm_program.py

```bash
python3 atm_program.pyc
```

## Donasi Pengembangan

Dukung kami dengan cara donasi ke Rekening dibawah ini, donasi anda sangat bermanfaat untuk pengembangan kami selanjutnya

```bash
DANA      : 085718683442

Briva BRI : 8881 0 0857 1868 3442

Briva BCA : 3901 0857 1868 3442
```

## Contact
WA : [RAFLI SETIAWAN](https://wa.me/6285702429294).

## Lisensi

ATMIN merupakan perangkat lunak bersumber terbuka yang dilisensikan di bawah [Lisensi MIT](https://opensource.org/licenses/MIT).