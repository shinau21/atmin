-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- current_timestamp() ON UPDATE current_timestamp()
-- Host: localhost:3306
-- Waktu pembuatan: 25 Apr 2020 pada 15.25
-- Versi server: 10.4.12-MariaDB-log
-- Versi PHP: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+07:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atmin`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `nasabah`
--

CREATE TABLE `nasabah`  (
  `rekening` int(10) NOT NULL PRIMARY KEY,
  `pin` varchar(8) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `jk` char(1) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `kec` varchar(100) NOT NULL,
  `kab` varchar(100) NOT NULL,
  `tempat_lahir` varchar(100) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `umur` int(3) NOT NULL,
  `nama_ibu` varchar(50) NOT NULL,
  `jenis` varchar(10) NOT NULL,
  `nik` varchar(16) NOT NULL,
  `kk` varchar(16) NOT NULL,
  `saldo_idr` varchar(101) NOT NULL,
  `saldo_usd` varchar(101) NOT NULL,
  `saldo_kwd` varchar(101) NOT NULL,
  `terakhir_akses` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Dump dari tabel `nasabah`
--

INSERT INTO `nasabah` (`rekening`, `pin`, `nama`, `jk`, `alamat`, `kec`, `kab`, `tempat_lahir`, `tanggal_lahir`, `umur`, `nama_ibu`, `jenis`, `nik`, `kk`, `saldo_idr`, `saldo_usd`, `saldo_kwd`) VALUES
('1234567890', '12121212', 'RAFLI SETIAWAN', 'L', 'RAKIT RT 02 / RW 03', 'RAKIT', 'BANJARNEGARA', 'BANJARNEGARA', '2000-04-18', '20', 'SITI MARKHATUN', 'member', '1234567890123456', '0987654321098765', '10000000', '100.00', '1000.00'),
('1234567891', '12121212', 'PROGATE INDONESIA', 'L', 'RAKIT RT 02 / RW 03', 'RAKIT', 'BANJARNEGARA', 'BANJARNEGARA', '2000-04-18', '20', 'SITI MARKHATUN', 'member', '1234567890123456', '0987654321098765', '10000000', '110.00', '1000.00');


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
