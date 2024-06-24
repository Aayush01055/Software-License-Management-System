create database ameya;

CREATE TABLE `brillentsec` (
  `SrNo` int NOT NULL AUTO_INCREMENT,
  `SerialNumber` varchar(500) NOT NULL,
  `CompName` varchar(500) NOT NULL,
  `ActivationCode` varchar(500) NOT NULL,
  `ExpiryDate` varchar(500) NOT NULL,
  `StartDate` varchar(500) NOT NULL,
  `CheckedOn` varchar(500) NOT NULL,
  `MacAddress` varchar(300) NOT NULL,
  `Activated` varchar(500) NOT NULL,
  `CheckedDt` varchar(500) NOT NULL,
  PRIMARY KEY (`SrNo`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `feedcalcusers` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(500) DEFAULT NULL,
  `password` varchar(500) DEFAULT NULL,
  `confirm_password` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
