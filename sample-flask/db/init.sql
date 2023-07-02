CREATE DATABASE IF NOT EXISTS develop;
USE develop;

CREATE TABLE IF NOT EXISTS visits (
  count INT
);

INSERT IGNORE INTO visits (count) VALUES (0);

