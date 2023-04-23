import os
import mysql.connector
from dotenv import load_dotenv


def create_connection(host_name, database, user_name, user_password):
    try:
        connection = mysql.connector.connect(host=host_name,
                                             database=database,
                                             user=user_name,
                                             password=user_password)
        print(f"Connection to MySQL DB '{database}' successful.")
    except mysql.connector.Error as err:
        return print(f"The error '{err}' occurred")
    return connection


def find_user_id_by_phone(cnx: mysql.connector, phone_number: str) -> int:
    get_user_id = ("SELECT user_id FROM user "
                   "WHERE phone = %s")
    cursor = cnx.cursor()
    cursor.execute(get_user_id, (phone_number, ))
    user_id = cursor.fetchall()[0][0]
    return user_id


def find_box_id(cnx: mysql.connector, user_id: int, data_box) -> int:
    get_box_id = ("SELECT box_id FROM box "
                  "WHERE (user_id = %s AND created_at = %s AND finished_at = %s)")
    cursor = cnx.cursor()
    cursor.execute(get_box_id, (user_id, data_box[1], data_box[2]))
    box_id = cursor.fetchall()[0][0]
    return box_id


def put_items_in_storage(cnx: mysql.connector,
                         data_user: list,
                         data_box: list,
                         data_stuff: list):  # не работает
    cursor = cnx.cursor()

    add_user = ("INSERT INTO user "
                "(nickname, phone, adress) "
                "VALUES (%s, %s, %s)")
    add_box_for_user = ("INSERT INTO box "
                        "(box_name, user_id, created_at, finished_at, items_size, items_weight, salt, encrypted_key) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    add_stuff_in_box = ("INSERT INTO stuff "
                        "(box_id, item_name) "
                        "VALUES (%s, %s)")

    user_id = find_user_id_by_phone(cnx, data_user[1])
    box_id = find_box_id(cnx, user_id, data_box)

    cursor.execute(add_user, data_user)
    data_box.insert(1, user_id)
    cursor.execute(add_box_for_user, data_box)
    for item in data_stuff:
        cursor.execute(add_stuff_in_box, (box_id, item))
    cnx.commit()


def main():
    load_dotenv()
    data_user = ["One more name", "89123456789", "г. Самара"]
    data_box = ['Название бокса', "2023-04-16", "2024-04-16", 8, 5, '', '']
    data_stuff = ["лыжи", "сноуборд", "мяч"]
    cnx = create_connection("localhost", "self_storage", "root",
                            os.environ['USER_PASSWORD'])
    put_items_in_storage(cnx, data_user, data_box, data_stuff)


if __name__ == '__main__':
    main()
