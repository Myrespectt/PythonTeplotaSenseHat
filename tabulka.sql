CREATE TABLE zaznam (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cas DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    teplota FLOAT NOT NULL,
    vlhkost FLOAT NOT NULL
) 