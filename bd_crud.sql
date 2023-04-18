CREATE DATABASE self_storage;
USE self_storage;

CREATE TABLE user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(20),
    phone INT(11)
);

CREATE TABLE storage(
    storage_id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    created_at DATE,
    finished_at DATE,
    box_width DECIMAL(2, 2),
    box_height DECIMAL(2, 2),
    box_length DECIMAL(2, 2),
    box_weight DECIMAL(4, 2)
);


/*Положить в хранилище*/
INSERT INTO user(nickname, phone)
VALUES ("Name", 89123456789);

INSERT INTO storage(
    created_at, finished_at, box_width,
    box_height, box_length, box_weight
    )
VALUES (2023-04-16, 2024-04-16, 10, 5, 20, 2.5);

/*Забрать все вещи.
Поиск по user_id. Но если у одного клиента несколько хранилищ
добавить поиск по связке user_id c storage_id*/

DELETE FROM storage
WHERE user_id = 1 AND storage_id = 4;

/*Продлить срок хранения*/
UPDATE storage
SET finished_at = 2025-04-16
WHERE user_id = 1 AND storage_id = 4;

/*Отчет по просроченной finished_at дате*/
