import base64

from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Random import get_random_bytes


class Encrypt:
    @staticmethod
    def encrypt(text: str, password: str):

        password_b64 = base64.b64encode(password.encode("utf-8"))
        password_md5 = MD5.new(password_b64).digest()
        iv = get_random_bytes(16)

        text = base64.b64encode(text.encode("utf-8"))
        pad = 16 - len(text) % 16
        text_b64 = text + b" " * pad

        encryptor = AES.new(password_md5, AES.MODE_CBC, iv)
        text_b64 = base64.b64encode(encryptor.encrypt(text_b64))

        return text_b64, iv

    @staticmethod
    def decrypt(encrypted_text: bytes, iv: bytes, password: str):

        password_b64 = base64.b64encode(password.encode("utf-8"))
        password_md5 = MD5.new(password_b64).digest()

        encrypted_b64 = base64.b64decode(encrypted_text)

        decryptor = AES.new(password_md5, AES.MODE_CBC, iv)
        text_b64 = decryptor.decrypt(encrypted_b64)

        try:
            text = base64.b64decode(text_b64)
            return text.decode("utf-8")
        except:
            return False
