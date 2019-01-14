import hashlib
import secrets

def generate_block_key(password: bytearray, blocId: bytearray, uniqueSignature: bytearray) -> bytearray:
    inputCombination: bytearray = uniqueSignature + password + blocId
    return sha_512_Hash(inputCombination)

def generate_unqiue_signature(n: int) -> bytearray:
    return secrets.token_bytes(n)

def sha_512_hash(input: bytearray) -> bytearray:
    return hashlib.sha512().update(input).digest()