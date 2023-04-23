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


def put_items_in_storage(cnx: mysql.connector,
                         data_user: list,
                         data_box: list):  # не работает
    cursor = cnx.cursor()

    add_user = ("INSERT INTO user "
                "(nickname, phone, adress) "
                "VALUES (%s, %s, %s)")
    get_user_id = ("SELECT user_id FROM user "
               "WHERE nickname = %s AND phone = %s")
    user_id = cursor.execute(get_user_id, data_user[:1])
    data_box.insert(1, user_id)
    add_box_for_user = ("INSERT INTO box "
                        "(box_name, user_id, created_at, finished_at, items_size, items_weight, salt, encrypted_key) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(add_user, data_user)
    cursor.execute(add_box_for_user, data_box)
    cnx.commit()
    cursor.exit()


def main():
    load_dotenv()
    data_user = ["One more name", "89111111111", "г. Самара"]
    data_box = ['Название бокса', "2023-04-16", "2024-04-16", 8, 5, '', '']
    cnx = create_connection("localhost", "self_storage", "root",
                            os.environ['USER_PASSWORD'])
    print(type(cnx))
    put_items_in_storage(cnx, data_user, data_box)


if __name__ == '__main__':
    main()
