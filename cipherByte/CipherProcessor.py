from cipherByte import KeyFactory
import math

def encrypt(data: bytearray, password: str):

    unique_signature: bytearray = KeyFactory.generate_unqiue_signature(25)
    total_blocks: int = (int)(math.ceil(data.len() / 64.0)) # each block is 64 bytes
    data_shift_position: int = 0

    for blockNumber in range(0, total_blocks):
        block_id: bytearray = bytearray(str(blockNumber))
        block_key: bytearray = KeyFactory.generate_block_key(unique_signature, bytearray(password), block_id)

        for i in range(0, block_key.len()) and data_shift_position < data.len():
            data[data_shift_position] = bytearray(data[data_shift_position] ^ block_key[i])
            data_shift_position += 1

    return unique_signature + data

def decrypt(data: bytearray, password: str):
    unique_signature: bytearray = data[:25]
    data = data[25:]

    total_blocks: int = (int)(math.ceil(data.len() / 64.0))  # each block is 64 bytes
    data_shift_position: int = 0

    for blockNumber in range(0, total_blocks):
        block_id: bytearray = bytearray(str(blockNumber))
        block_key: bytearray = KeyFactory.generate_block_key(unique_signature, bytearray(password), block_id)

        for i in range(0, block_key.len()) and data_shift_position < data.len():
            data[data_shift_position] = bytearray(data[data_shift_position] ^ block_key[i])
            data_shift_position += 1

    return data