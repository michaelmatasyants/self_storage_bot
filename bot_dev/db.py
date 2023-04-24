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


def create_user(cnx: mysql.connector, data_user) -> None:
    add_user = ("INSERT INTO user "
                "(tg_user_name, nickname, phone, adress) "
                "VALUES (%s, %s, %s, %s)")
    cursor = cnx.cursor()
    cursor.execute(add_user, data_user)
    cnx.commit()

def create_box()  -> None:
    pass


def get_user_boxes(user_id: int) -> list[tuple]:
    pass


def get_box(box_id: int) -> tuple:
    pass


def delete_box(box_id: int) -> None:
    pass

 
def get_overdue_boxes() -> list[tuple]:
    pass


def get_overdue_box(box_id: int):
    return user.phone, box.finished_at, 'etc..'


def get_all_boxes() -> list[tuple]:
    pass
