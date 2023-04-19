from pathlib import Path
import hashlib
import secrets
import qrcode
import cv2
import ast


def encrypt(any_id: str) -> dict:
    salt = secrets.token_bytes(32)
    encrypt_key = hashlib.pbkdf2_hmac("sha256", bytes(any_id, "utf-8"),
                                      salt, 10000)
    return {
        "salt": salt,
        "encrypted_key": encrypt_key
        }


def get_storage_info(encrypted_storage_id: dict,
                     pick_up_stuff=None,
                     add_stuff=None) -> dict:
    # get list of stuff to add or/and remove from to the box from the bot
    storage_info = encrypted_storage_id
    if pick_up_stuff is not None:
        storage_info["pick_up_stuff"] = pick_up_stuff
    if add_stuff is not None:
        storage_info["add_stuff"] = add_stuff
    return storage_info


def generate_qr(storage_info: dict) -> qrcode.image:
    qr = qrcode.QRCode(
        version=None,  # size is choosen automatically
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.add_data(storage_info)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    return image


def is_qr_valid(data_qr: dict, data_db: dict) -> True:
    # compare "salt" and "encrypt_key" from DB to make sure qr is valid
    if (data_qr.get('salt') == data_db.get('salt')
            and data_qr.get('encrypt_key') == data_db.get('encrypt_key')):
        return True


def decode_qr(image) -> dict:
    detector = cv2.QRCodeDetector()
    data_qr, vertex_array, binary_qr = detector.detectAndDecode(image)
    return ast.literal_eval(data_qr)


def update_stuff_db(data_qr):  # сhange the list of stuff in the box in the DB
    pass


def main():
    storage_id = str(1248125812)
    pick = ["лыжи", "сноуборд"]  # get a list of things to pick up from the bot
    add = ["мяч", "книги"]  # get a list of things to add from the bot
    encrypted_id = encrypt(storage_id)
    storage_info = get_storage_info(encrypted_id, pick, add)
    generate_qr(storage_info).save('stuff_qr.png')
    # add "encrypt_key" and "salt" to DB after generating the qr

    image = cv2.imread(str(Path('stuff_qr.png')))
    data_qr = decode_qr(image)
    data_db = encrypted_id

    if is_qr_valid(data_qr, data_db):  # scan qr, open box for client
        update_stuff_db(data_qr)  # сhange list of stuff in the box in the DB
        return print("QR code is valid")
    return print("QR code is invalid")


if __name__ == "__main__":
    main()
