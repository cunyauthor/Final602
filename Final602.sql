USE SYS;
 
Drop Table If Exists WageByState;
 
CREATE TABLE WageByState
(
  `AREA` varchar(100) NOT NULL,
  `ST` varchar(100) NOT NULL,
  `STATE` varchar(100) NOT NULL,
  `OCC_CODE` varchar(100) NOT NULL,
  `OCC_TITLE` varchar(100) NOT NULL,
  `OCC_GROUP` varchar(100) NOT NULL,
  `TOT_EMP` varchar(100) NOT NULL,
  `EMP_PRSE` varchar(100) NOT NULL,
  `JOBS_1000` varchar(100) NOT NULL,
  `LOC_Q` varchar(100) NOT NULL,
  `H_MEAN` varchar(100) NOT NULL,
  `A_MEAN` varchar(100) NOT NULL,
  `MEAN_PRSE` varchar(100) NOT NULL,
  `H_PCT10` varchar(100) NOT NULL,
  `H_PCT25` varchar(100) NOT NULL,
  `H_MEDIAN` varchar(100) NOT NULL,
  `H_PCT75` varchar(100) NOT NULL,
  `H_PCT90` varchar(100) NOT NULL,
  `A_PCT10` varchar(100) NOT NULL,
  `A_PCT25` varchar(100) NOT NULL,
  `A_MEDIAN` varchar(100) NOT NULL,
  `A_PCT75` varchar(100) NOT NULL,
  `A_PCT90` varchar(100) NOT NULL,
  `ANNUAL` varchar(100) NOT NULL,
  `HOURLY` varchar(100) NOT NULL
);
 
SELECT * FROM WageByState;
 
LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm15st/state_M2015_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
 
;
 
SELECT * FROM WageByState ;
SELECT COUNT(*) FROM WageByState;