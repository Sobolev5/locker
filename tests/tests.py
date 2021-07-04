from encrypt.Encrypt import Encrypt


def test_encode_decode():
    # python run.py tests.tests "test_encode_decode()"
    text = "Test text"
    password = "Text password"
    encrypted_b64, iv_b64 = Encrypt.encrypt(text, password)
    decrypted_text = Encrypt.decrypt(encrypted_b64, iv_b64, password)
    assert text == decrypted_text
