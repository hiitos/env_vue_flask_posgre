USE work_db;

-- CREATE TABLE IF NOT EXISTS sample_table(
--   `id`         int(11) NOT NULL AUTO_INCREMENT,
--   `sample`     text,
--   PRIMARY KEY (`id`)
-- ) character set utf8mb4;

CREATE TABLE sample_table(
  `id`         int(11) NOT NULL AUTO_INCREMENT,
  `sample`     text,
  PRIMARY KEY (`id`)
) character set utf8mb4;


INSERT INTO 
    sample_table (sample)
VALUES 
    ("sample1"),
    ("sample2")
;