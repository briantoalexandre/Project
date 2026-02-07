-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Dim 11 Septembre 2011 à 22:59
-- Version du serveur: 5.1.41
-- Version de PHP: 5.3.2-1ubuntu4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `emploibois`
--

-- --------------------------------------------------------

--
-- Structure de la table `employes`
--

CREATE TABLE IF NOT EXISTS `employes` (
  `EMPNO` int(2) NOT NULL,
  `EMPNOM` varchar(30) NOT NULL,
  `EMPPREN` text NOT NULL,
  `EMPSEXE` char(1) NOT NULL,
  `EMPSALAIRE` int(7) NOT NULL,
  `EMPPRIME` int(7) NOT NULL,
  `SRVNO` int(2) NOT NULL,
  PRIMARY KEY (`EMPNO`),
  KEY `SRVNO` (`SRVNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `employes`
--

INSERT INTO `employes` (`EMPNO`, `EMPNOM`, `EMPPREN`, `EMPSEXE`, `EMPSALAIRE`, `EMPPRIME`, `SRVNO`) VALUES
(1, 'LEBOSS', 'GILLES', 'M', 45000, 5000, 1),
(2, 'ORGAN', 'INGRID', 'F', 35000, 5555, 1),
(3, 'DUPLAFOND', 'GREGOIRE', 'M', 35000, 5555, 1),
(4, 'VENDUE', 'ROSALIE', 'F', 20000, 1000, 2),
(5, 'DUDESERT', 'RAISSA', 'F', 20000, 1000, 2),
(6, 'LEBLOND', 'BERTRAND', 'M', 6000, 500, 2),
(7, 'LABELLE', 'REINE', 'F', 18000, 1000, 3),
(8, 'LEDUR', 'ALAIN', 'M', 10000, 4500, 3),
(9, 'DUPONT', 'INES', 'F', 6000, 1000, 3),
(10, 'DUMONT', 'ADELPHE', 'M', 15000, 1500, 4),
(11, 'LEROUX', 'APOLLINAIRE', 'M', 10000, 2000, 4),
(12, 'LEDUR', 'AIME', 'M', 6500, 100, 4),
(13, 'LEBON', 'ROLAND', 'M', 6000, 500, 4),
(14, 'LABRUTE', 'EDITH', 'F', 5500, 100, 4),
(15, 'DESTIN', 'RENAUD', 'M', 16000, 1000, 5),
(16, 'DUJARDIN', 'NADEGE', 'F', 4000, 1000, 5),
(17, 'BRILLES', 'EMILIE', 'F', 5000, 200, 5),
(18, 'LEBRUN', 'DAVY', 'M', 4800, 1000, 5),
(19, 'LEGRAND', 'MATTHIEU', 'M', 5000, 1000, 5),
(20, 'DESPLANTES', 'MAURICE', 'M', 6600, 555, 6);

-- --------------------------------------------------------

--
-- Structure de la table `intervenir`
--

CREATE TABLE IF NOT EXISTS `intervenir` (
  `PROJNO` int(2) NOT NULL,
  `EMPNO` int(2) NOT NULL,
  `NBHEURES` int(4) NOT NULL,
  PRIMARY KEY (`PROJNO`,`EMPNO`),
  KEY `EMPNO` (`EMPNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `intervenir`
--

INSERT INTO `intervenir` (`PROJNO`, `EMPNO`, `NBHEURES`) VALUES
(1, 9, 15),
(1, 13, 8),
(1, 14, 8),
(1, 15, 24),
(1, 17, 50),
(2, 14, 70),
(2, 19, 70),
(2, 20, 70),
(3, 6, 10),
(3, 14, 6),
(3, 15, 80),
(3, 20, 85);

-- --------------------------------------------------------

--
-- Structure de la table `projets`
--

CREATE TABLE IF NOT EXISTS `projets` (
  `PROJNO` int(2) NOT NULL,
  `PROJLIB` varchar(11) NOT NULL,
  `SRVNO` int(2) NOT NULL,
  PRIMARY KEY (`PROJNO`),
  KEY `SRVNO` (`SRVNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `projets`
--

INSERT INTO `projets` (`PROJNO`, `PROJLIB`, `SRVNO`) VALUES
(1, 'CENTREVILLE', 5),
(2, 'NOUVPISCINE', 4),
(3, 'EAUPURIFIEE', 6);

-- --------------------------------------------------------

--
-- Structure de la table `services`
--

CREATE TABLE IF NOT EXISTS `services` (
  `SRVNO` int(2) NOT NULL,
  `SRVNOM` varchar(30) NOT NULL,
  PRIMARY KEY (`SRVNO`),
  UNIQUE KEY `SRVNOM` (`SRVNOM`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `services`
--

INSERT INTO `services` (`SRVNO`, `SRVNOM`) VALUES
(2, 'COMMERCIAL'),
(3, 'COMPTABILITE'),
(1, 'DIRECTION'),
(6, 'ESPACES VERTS'),
(5, 'MACONNERIE'),
(4, 'TERRASSEMENT');

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `employes`
--
ALTER TABLE `employes`
  ADD CONSTRAINT `employes_ibfk_1` FOREIGN KEY (`SRVNO`) REFERENCES `services` (`SRVNO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `intervenir`
--
ALTER TABLE `intervenir`
  ADD CONSTRAINT `intervenir_ibfk_1` FOREIGN KEY (`PROJNO`) REFERENCES `projets` (`PROJNO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervenir_ibfk_2` FOREIGN KEY (`EMPNO`) REFERENCES `employes` (`EMPNO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `projets`
--
ALTER TABLE `projets`
  ADD CONSTRAINT `projets_ibfk_1` FOREIGN KEY (`SRVNO`) REFERENCES `services` (`SRVNO`) ON DELETE CASCADE ON UPDATE CASCADE;
