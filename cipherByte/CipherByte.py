from cipherByte import CipherProcessor


def encrypt(data: bytearray, password: str):
    return CipherProcessor.encrypt(data, password)


def decrypt(data: bytearray, password: str):
    return CipherProcessor.decrypt(data, password)
