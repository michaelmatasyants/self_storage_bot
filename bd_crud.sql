CREATE DATABASE self_storage;
USE self_storage;

CREATE TABLE user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    tg_username VARCHAR(20),
    nickname VARCHAR(20),
    phone VARCHAR(11),
    adress VARCHAR(80)
);

CREATE TABLE box(
    box_id INT PRIMARY KEY AUTO_INCREMENT,
    box_name VARCHAR(30),
    user_id INT NOT NULL,
    created_at DATE,
    finished_at DATE,
    items_size DECIMAL(4, 2),
    items_weight DECIMAL(4, 2),
    salt VARCHAR(32),
    encrypted_key VARCHAR(32),
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE CASCADE
);


CREATE TABLE stuff(
    stuff_id INT PRIMARY KEY AUTO_INCREMENT,
    box_id INT NOT NULL,
    user_id INT NOT NULL,
    item_name VARCHAR(30),
    FOREIGN KEY (box_id) REFERENCES box (box_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE CASCADE
);

/*Положить в хранилище
Обратить внимание на момент добавление адреса в БД.
Решить откуда будем брать box_name и на каком этапe. Например, box_name = сцепка первой вещи
и дата создания box-а, либо давать возможность назначать box_name пользователю.*/

INSERT INTO user(tg_username, nickname, phone, adress)
VALUES ("@tg_username", "Name", "89123456789", "г. Санкт-Петербрг, улица Чайковского, д.62, кв.13");

SET @user_id = (
    SELECT user_id FROM user
    WHERE tg_username = '@tg_username'
);

INSERT INTO box(box_name, user_id, created_at, finished_at, items_size, items_weight,
                salt, encrypted_key)
VALUES ('', @user_id, "2023-04-16", "2024-04-16", 8, 5, '', '');

SET @box_id = (
    SELECT box_id
    FROM box
    WHERE (user_id = @user_id AND created_at = "2023-04-16"
           AND finished_at = "2024-04-16" AND items_size = 8
           AND items_weight = 5)
);


INSERT INTO stuff (box_id, user_id, item_name)
VALUES (@box_id, @user_id, "лыжи"),
       (@box_id, @user_id, "сноуборд"),
       (@box_id, @user_id, "мяч")
;

/* Генерация QR кода. Добавление "encrypted_key" и "salt" в "box".
Тянем из бота "box_id" */

UPDATE box
SET salt = "12345678123456781234567812345678",
    encrypted_key = "12345678123456781234567812345678"
WHERE box_id = 1;
UPDATE box
SET salt = "87654321876543218765432187654321",
    encrypted_key = "87654321876543218765432187654321"
WHERE box_id = 2;

/*Получение из БД "box_id" и "user_id" по 
"encrypted_key" и "salt" при сканировании QR*/

SET @qr_box_id = (
    SELECT box_id FROM box
    WHERE (encrypted_key = 12345678123456781234567812345678
            AND salt = 12345678123456781234567812345678)
);

SET @qr_user_id = (
    SELECT user_id FROM box
    WHERE (box_id = @qr_box_id)
);

/*получить stuff_id по box_id выбранной вещи, которую надо забрать
(последнее получаем из бота или из QR, например 'лыжи').*/

SELECT stuff_id FROM stuff
WHERE box_id = @qr_box_id AND stuff = 'лыжи';


/*Забрать все вещи без возврата.
После скана QR удаляется список вещей у конкретного 
user_id с конкретным box_id (получили на предыдущем шаге)*/

DELETE FROM stuff
WHERE box_id = @qr_box_id;

DELETE FROM box
WHERE user_id = @qr_user_id AND box_id = @qr_box_id;

/*Забрать некоторые вещи из списка (например лыжи)*/
DELETE FROM stuff
WHERE box_id = @qr_box_id AND stuff_id in (
    SELECT stuff_id FROM stuff
    WHERE box_id = @qr_box_id AND stuff = 'лыжи'
);

/*Добавить вещи в существующий бокс.
В ДОЛГИЙ ЯЩИК, ДОПИЛИТЬ: вещи, которые взяли, но вернут позже, добавляются в отдельную
таблицу HOLD и живут там пока их не вернут из HOLD в stuff,
или не заберут все остальные из stuff*/
INSERT INTO stuff (box_id, item_name)
VALUES ('получаем @box_id при скане qr', 'название вещи получаем при скане qr');

/*Список боксов клиента для вывода в боте.*/
SELECT box_name
FROM box
WHERE user_id = 'получаемый user_id из бота';

/*Список вещей в box для вывода в боте*/
SELECT item_name
FROM stuff
WHERE box_id = 'получаемый box_id из бота';

/*Продлить срок хранения до 2025-04-16 (дату берем из бота)*/
UPDATE storage
SET finished_at = "2025-04-16"
WHERE user_id = 1 AND box_id = 4;

/*Отчет по просроченной finished_at дате (Список user_id и box_id по которым есть просрочка*/

SELECT tg_username, nickname, box_id, finished_at, phone, adress,
       DATEDIFF(CURDATE(), finished_at) AS overdue_days
FROM user INNER JOIN box ON user.user_id = box.user_id
WHERE DATEDIFF(CURDATE(), finished_at) > 0;