-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2024 at 03:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

CREATE DATABASE IF NOT EXISTS itl;
USE itl;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- Drop existing tables
DROP TABLE IF EXISTS `carrera`;
DROP TABLE IF EXISTS `especialidad`;
DROP TABLE IF EXISTS `materia`;

-- Table structure for table `carrera`
CREATE TABLE `carrera` (
  `CarreraID` varchar(10) NOT NULL,
  `NombreCarrera` varchar(100) NOT NULL,
  `Semestres` int(2) NOT NULL,
  `EspecialidadID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `especialidad`
CREATE TABLE `especialidad` (
  `EspecialidadID` varchar(10) NOT NULL,
  `NombreEspecialidad` varchar(100) NOT NULL,
  `CarreraID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `materia`
CREATE TABLE `materia` (
  `MateriaID` varchar(10) NOT NULL,
  `NombreMateria` varchar(100) NOT NULL,
  `Creditos` int(2) NOT NULL,
  `CarreraID` varchar(10) NOT NULL,
  `Semestre` int(2) NOT NULL,
  `Seguimiento` varchar(100) NOT NULL,
  `EspecialidadID` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;
