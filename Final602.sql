USE SYS;
 
Drop Table If Exists WageByState;
Drop Table If Exists State;
 
CREATE TABLE State
( 
	`State` varchar(100) NOT NULL
);
 
SELECT * FROM State;
 
LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/State.csv"
INTO TABLE State
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
 
;
 
SELECT * FROM State ;
SELECT COUNT(*) FROM State;


CREATE TABLE WageByState
(
  `MyYear` varchar(4) NOT NULL,
  `AREA` varchar(100) NOT NULL,
  `ST` varchar(100) NOT NULL,
  `STATE` varchar(100) NOT NULL,
  `OCC_CODE` varchar(100) NOT NULL,
  `OCC_TITLE` varchar(100) NOT NULL,
  `OCC_GROUP` varchar(100) NOT NULL,
  `TOT_EMP` varchar(100) NOT NULL,
  `A_MEAN` varchar(100) NOT NULL
);
 
SELECT * FROM WageByState ;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm15st/state_M2015_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm14st/state_M2014_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm13st/state_M2013_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm12st/state_M2012_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm11st/state_M2011_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm10st/state_M2010_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm09st/state_M2009_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm08st/state_M2008_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm07st/state_M2007_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm06st/state_M2006_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

LOAD DATA LOCAL INFILE "/Users/fionaho/Desktop/Final Project 602/oesm05st/state_M2005_dl.csv"
INTO TABLE WageByState
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;
 
SELECT * FROM WageByState where occ_title like 'Appraisers and Assessors of Real Estate'  ;
SELECT COUNT(*) FROM WageByState;

Delete from WageByState where MyYear='2013';