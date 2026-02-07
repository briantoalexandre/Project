CREATE DATABASE immodb;

use immodb;

CREATE TABLE `appartement` (
  `a_code` int(11) NOT NULL,
  `a_loyer` int(11) NOT NULL,
  `a_superf` int(11) NOT NULL,
  `a_etat` varchar(20) NOT NULL,
  `imm_num` int(11) NOT NULL,
  `t_code` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `appartement` (`a_code`, `a_loyer`, `a_superf`, `a_etat`, `imm_num`, `t_code`) VALUES
(101, 800, 75, 'BON', 1, 1),
(102, 700, 60, 'MOYEN', 2, 2),
(103, 650, 55, 'BON', 2, 2),
(104, 750, 70, 'TBE', 2, 1),
(111, 500, 32, 'BON', 2, 3),
(112, 500, 30, 'MOYEN', 2, 6),
(115, 600, 50, 'VETUSTE', 5, 2),
(155, 850, 85, 'MOYEN', 7, 1),
(203, 650, 50, 'MOYEN', 4, 2),
(205, 550, 30, 'VETUSTE', 4, 3),
(211, 650, 45, '', 5, 2),
(303, 1000, 95, 'BON', 7, 7),
(305, 750, 77, 'BON', 4, 1),
(306, 950, 90, 'TBE', 3, 4),
(307, 550, 33, 'TBE', 1, 5);


CREATE TABLE `immeuble` (
  `imm_num` int(11) NOT NULL,
  `imm_nbetage` int(11) NOT NULL,
  `imm_code` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `immeuble` (`imm_num`, `imm_nbetage`, `imm_code`) VALUES
(1, 5, '3027'),
(2, 3, '3142'),
(3, 2, '5628'),
(4, 5, '1198'),
(5, 5, '3388'),
(6, 7, '1989'),
(7, 3, '2077'),
(8, 5, ''),
(9, 5, '2001'),
(10, 6, '1515');

CREATE TABLE `type_app` (
  `t_code` int(11) NOT NULL,
  `t_nom` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `type_app` (`t_code`, `t_nom`) VALUES
(1, 'T4'),
(2, 'T3'),
(3, 'T2'),
(4, 'F4'),
(5, 'F3'),
(6, 'F2'),
(7, 'F5');

ALTER TABLE `appartement`
  ADD PRIMARY KEY (`a_code`),
  ADD KEY `fk` (`t_code`),
  ADD KEY `fk1` (`imm_num`);


ALTER TABLE `immeuble`
  ADD PRIMARY KEY (`imm_num`);


ALTER TABLE `type_app`
  ADD PRIMARY KEY (`t_code`);


ALTER TABLE `appartement`
  ADD CONSTRAINT `fk` FOREIGN KEY (`t_code`) REFERENCES `type_app` (`t_code`),
  ADD CONSTRAINT `fk1` FOREIGN KEY (`imm_num`) REFERENCES `immeuble` (`imm_num`);
COMMIT;

