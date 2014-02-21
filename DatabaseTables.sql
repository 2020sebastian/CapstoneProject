drop table Sokographs;
drop table Words;
drop table userid;

create table Sokographs (
  
  sokographID number(10),
  word varchar(15),
  coordinates number(10),
  
  primary key (sokgraphID)
  );
  
create table Words (

  words varchar(15),
  w_length number(10),
  
  primary key (words)
  );
  
create table userid (

  user_ID number(10),
  kb_choice number(2),
  
  primary key (user_ID)
  );