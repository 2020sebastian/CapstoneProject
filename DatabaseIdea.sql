CREATE TABLE Filter1
(
  word varchar(20) NOT NULL,
  beginX number(5) NOT NULL,
  beginY number(5) NOT NULL,
  endX number(5) NOT NULL,
  endY number(5) NOT NULL,
  sokgraphL number(20) NOT NULL,
  PRIMARY KEY (word)
);

CREATE TABLE Sokgraph
(
  word varchar(20) NOT NULL, 
  sokgraphL number(20) NOT NULL,//perfect sokgraph length for word
  x1 int,
  y1 int,
  x2 int,
  y2 int,
  x3 int,
  y3 int,
  x4 int,
  y4 int,
  x5 int,
  y5 int,
  x6 int,
  y6 int,
  x7 int,
  y7 int,
  x8 int,
  y8 int,
  x9 int,
  y9 int,
  x10 int,
  y10 int,
  x11 int,
  y11 int,
  x12 int,
  y12 int,
  x13 int,
  y13 int,
  x14 int,
  y14 int,
  x15 int,
  y15 int,
  x16 int,
  y16 int,
  x17 int,
  y17 int,
  x18 int,
  y18 int,
  x19 int,
  y19 int,
  x20 int,
  y20 int,
  PRIMARY KEY (word)
);

create table User (
  
   userID number(10),  
   userFreqWordList varchar(100), 
   userKBChoice varchar(20),
   primary key (userID)
);