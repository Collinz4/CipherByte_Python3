import hashlib
import secrets


def generate_block_key(password: bytearray, block_id: bytearray, unique_signature: bytearray) -> bytearray:
    input_combination: bytearray = unique_signature + password + block_id
    return hashlib.sha512().update(input_combination).digest()


def generate_unique_signature(n: int) -> bytearray:
    return secrets.token_bytes(n)
