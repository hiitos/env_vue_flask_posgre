use work_db;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL,
    email VARCHAR(32) NOT NULL,
    PRIMARY KEY (id)
) character set utf8mb4;

-- usersのテストデータ
INSERT INTO
    users (id,name,email) 
VALUES 
    (1, 'TOM','xxxx@mail.co.jp'),
    (2, 'Jonnnnn','Yxxx@mail.co.jp')
;
