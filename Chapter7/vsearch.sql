CREATE TABLE log (
  id int(11) NOT NULL AUTO_INCREMENT,
  ts timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  phrase varchar(128) NOT NULL,
  letters varchar(128) NOT NULL,
  ip varchar(16) NOT NULL,
  browser_string varchar(256) not null,
  results varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
);
describe log;

