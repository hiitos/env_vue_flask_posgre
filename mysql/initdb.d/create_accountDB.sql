use work_db;

CREATE TABLE `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_name` varchar(64) NOT NULL UNIQUE,
  `start_on` datetime NOT NULL,
  `end_on` datetime NOT NULL,
  `created_by` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`)
) character set utf8mb4;-- ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- account のテストデータ
INSERT INTO
    account (id,account_name, start_on, end_on, created_by, created_at,updated_by,updated_at,status)
VALUES
    -- ('sample_account','2021-01-01', '2021-12-31', 99, now(),0)
    (1, 'TOM',timestamp '2022-10-01 00:00:00',timestamp '2023-10-01 00:00:00',NULL,NULL,NULL,NULL,'1'),
    (2, 'John',timestamp '2022-10-02 00:00:00',timestamp '2023-10-02 00:00:00',NULL,NULL,NULL,NULL,'1'),
    (3, 'Mike',timestamp '2022-10-03 00:00:00',timestamp '2023-10-03 00:00:00',NULL,NULL,NULL,NULL,'1')
;

insert into 
    account (account_name, start_on, end_on, created_by, created_at, status) 
values
    ('sample_account','2021-01-01', '2021-12-31', 99, now(),0)
;