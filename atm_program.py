U
    �$�_�!  �                   @   s�  d dl Z d dlZd dlZd dlmZ d dlmZ d dlmZmZ d dl	m
Z
 e
d�Zdd� Zd	d
� Ze�ejd� e�  e�  eed��Zeed��Zd Zee�� kr�ee�� kr�edk r�e�  e�  ed� eed��Zed7 Zedkr�ed� e�  q�ee�� krree�� krre�  e�  ed� ed� ed� ed� ed� ed� ed� ed�Zedk�r�e�  e�  e�� Ze�� Ze�� Zedd� e�� edd� e�� edd� e�� ed� q�edk�re�  e�  ed� ed � ed!� ed� ed"�Z!e!dk�r�e�  e�  d#Z"ed$d� e"�� eed%��Z#e#e"k�r�e�� e#k�r�e�$e#� ed&e%e#�� ed'd� e�� �� ed� ned(� ed� n,d)Z&ed*� ed+� ed,d� e&�� ed� e!dk�r�e�  e�  d-Z'ed.d� e'�� e(ed/��Z#e#e'k�r\e�� e#k�rJe�)e#� ed0e%e#�� ed1d� e�� �� ed� ned2� ed� n*d3Z&ed*� ed+� ed4e%e&�� ed� e!d5k�r�e�  e�  d6Z*ed7e%e*� � e(ed8��Z#e#e*k�r�e�� e#k�r�e�+e#� ned9� ed� n*d6Z&ed*� ed+� ed:e%e&�� ed� q�ed5k�r$e�  e�  ed;� ed<� ed=� ed� ed"�Z,e,dk�r�e�  e�  eed>��Z#e�-e#� ed?d� e#� d@ � e,dk�r�e�  e�  e(edA��Z#e�.e#� edBd� e#� dC � e,d5k�r�e�  e�  eedD��Z#e�/e#� edEd� e#� dF � q�edGk�r�e�  e�  eedH��Z0e�� e0k�r�e�  e�  eedI��Z1e0e1k�r�e�2e1� e�  e�  edJe%e1� � ed� nedK� ed� nedL� ed� q�edMk�rRe�  e�  edN� edO� edP� edQe�3�  � edRe�4�  � edSe�5�  � edTe�6�  � edUe�7�  � ed� q�edVk�rxe�  e�  e�� Ze�� Ze�� ZedWdX�Z8e%e j �9� �Z:edYe%e8� � edZe: � edd� e�� edd� e�� edd� e�� e;d[d\�Z<e<�=d]� e<�=d^e%e8� d] � e<�=d_e: d] � e<�=dd� e� d] � e<�=dd� e� d] � e<�=dd� e� d] � e<�>�  e�  q�e�  e�  ed`� eda� ed� q�qrdS )b�    N)�sleep)�randint)�system�name)�Customer�   c                   C   s,   t d� t d� t d� t d� t d� d S )Nz0================================================z0            BANK  PELAJAR  INDONESIA            z*Copyright : RAFLI SETIAWAN (@shinau_store)� )�print� r
   r
   �atm_program.py�banner   s
    r   c                  C   s   t dkrtd�} ntd�} d S )N�nt�cls�clear)r   r   )�_r
   r
   r   r      s    
r   r   zMasukan Nomor Kartu Anda : zMasukan PIN Anda : �   z/PIN yang anda masukan salah, silahkan coba lagizMasukan Kembali PIN Anda : zError, Silahkan coba lagiz1. Cek Saldoz2. Tarik Saldoz3. Simpan Saldoz4. Ganti PINz5. Info Penggunaz	0. KeluarzMasukan Inputan (0-4) :�1zSaldo IDR : Rp.z{0:n}zSaldo USD : $zSaldo KWD : K.D �2z1. Tarik Saldo IDRz2. Tarik Saldo USDz3. Tarik Saldo KWDzMasukan Inputan Anda : iP�  z!Minimal Penarikan Saldo IDR = Rp.z(Masukan Nominal IDR Yang Akan Ditarik : zSaldo IDR Yang Anda Tarik : Rp.zSisa Saldo IDR Anda : Rp.z/Saldo IDR Tidak Cukup Untuk Melakukan PenarikaniO�  z)Nominal Yang Anda Masukan Terlalu SedikitzSilahkan Coba Lagiz7Pastikan Nominal Yang Anda Masukan Harus Lebih Dari Rp.g      $@zMinimal Penarikan Saldo USD = $z(Masukan Nominal USD Yang Akan Ditarik : zSaldo USD Yang Anda Tarik : Rp.zSisa Saldo USD Anda : Rp.z/Saldo USD Tidak Cukup Untuk Melakukan Penarikang{�G��#@z3Pastikan Nominal Yang Anda Masukan Harus Lebih Dari�3g      @zMinimal Penarikan Saldo KWD = z(Masukan Nominal KWD Yang Akan Ditarik : z/Saldo KWD Tidak Cukup Untuk Melakukan Penarikanz8Pastikan Nominal Yang Anda Masukan Harus Lebih Dari K.D.z1. Simpan Saldo IDRz2. Simpan Saldo USDz3. Simpan Saldo KWDz)Masukan Nominal IDR Yang Akan Disimpan : zRp.z" Berhasil Ditambahkan Ke Saldo IDRz)Masukan Nominal USD Yang Akan Disimpan : �$z" Berhasil Ditambahkan Ke Saldo USDz)Masukan Nominal KWD Yang Akan Disimpan : zK.D.z" Berhasil Ditambahkan Ke Saldo KWD�4zMasukan PIN Lama Anda : zMasukan PIN Baru Anda : zPIN baru anda : z0Anda tidak bisa membuat PIN baru dengan PIN lamaz PIN Lama Yang Anda Masukan Salah�5z===============================z       Informasi Nasabah       z ================================zNama     : zGender   : zMember   : zAlamat   : zNama Ibu : �0i�� i@B z	Record : zWaktu : zhistory.txt�a�
zRecord    : zWaktu     : z8Maaf input yang anda masukan tidak ada dalam daftar menuzSilahkan coba lagi)?Zdatetime�locale�os�timer   Zrandomr   r   r   Zcustomerr   Zatmr   r   �	setlocale�LC_ALL�int�inputZcardZpin�countZ	checkCardZcheckPinr	   �exitZpilZcheckIDRZ	saldo_idrZcheckUSDZ	saldo_usdZcheckKWDZ	saldo_kwd�formatZinp_tarZlmt_tidrZinp_nomZ
witdrawIDR�strZlmtZlmt_tusd�floatZ
witdrawUSDZlmt_tkwdZ
witdrawKWDZinp_simZ
depositIDRZ
depositUSDZ
depositKWDZp_verZgpZ	changePinZ	checkNameZcheckGenderZ
checkJenisZcheckAlamatZcheckIbuZrecZnow�date�open�file�write�closer
   r
   r
   r   �<module>   s|   



































