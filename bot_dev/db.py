import mysql.connector


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

# data_user = [tg_username, nickname, phone, adress]
def create_or_get_user(connection: mysql.connector,
                       data_user: list) -> int | None:
    tg_username = data_user[1]
    cursor = connection.cursor()
    try:
        get_user_id = ("SELECT user_id FROM user "
                       "WHERE tg_username = %s")
        cursor.execute(get_user_id, (tg_username, ))
        user_id = cursor.fetchall()[0][0]
        return user_id
    except mysql.connector.Error:
        add_user = ("INSERT INTO user "
                    "(tg_username, nickname, phone, adress) "
                    "VALUES (%s, %s, %s, %s)")
        cursor.execute(add_user, data_user)
        connection.commit()


# data_box = [box_name, created_at, finished_at, items_size, items_weight, salt, encrypted_key]
def create_box(connection: mysql.connector, data_user: list, data_box: list):
    user_id = create_or_get_user(connection, data_user)
    data_box.insert(1, user_id)
    add_box_for_user = ("INSERT INTO box "
                        "(box_name, user_id, created_at, finished_at, items_size, items_weight, salt, encrypted_key) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor = connection.cursor()
    cursor.execute(add_box_for_user, data_box)
    connection.commit()


def get_user_boxes(user_id: int) -> list[tuple]:
    pass


def get_box(box_id: int) -> tuple:
    pass


def delete_box(box_id: int) -> None:
    pass

 
def get_overdue_boxes() -> list[tuple]:
    pass


def get_overdue_box(box_id: int):
    return # user.phone, box.finished_at, 'etc..'


def get_all_boxes() -> list[tuple]:
    pass

