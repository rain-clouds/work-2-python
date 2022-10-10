import socket

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def my_xor_on_bytes(bytes1, bytes2):
    xor_bytes = bytes(bytes2[i] ^ b for i, b in enumerate(bytes1))
    return xor_bytes


def crypt_block(plain_text_block, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(plain_text_block)


def decrypt_block(cyper_text_block, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(cyper_text_block)


def crypt_ecb(plain_text, key):
    block = plain_text[0:16:1]
    cypher = b''
    while len(plain_text) > 0:
        cypher += crypt_block(block, key)
        plain_text = plain_text[16::1]
        block = plain_text[0:16:1]
    return cypher


def decrypt_ecb(cyper_text, key):
    block = cyper_text[0:16:1]
    plain_text = b''
    while len(cyper_text) > 0:
        plain_text += decrypt_block(block, key)
        cyper_text = cyper_text[16::1]
        block = cyper_text[0:16:1]
    return plain_text


def crypt_cbc(plain_text, key, iv):
    block = plain_text[0:16:1]
    cypher = b''
    while len(plain_text) > 0:
        block_xor = my_xor_on_bytes(block, iv)
        crypted_block = crypt_block(block_xor, key)
        cypher += crypted_block
        iv = crypted_block
        plain_text = plain_text[16::1]
        block = plain_text[0:16:1]
    return cypher


def decrypt_cbc(cypher_text, key, iv):
    block = cypher_text[0:16:1]
    plain_text = b''
    while len(cypher_text) > 0:
        decrypted_block = decrypt_block(block, key)
        block_xor = my_xor_on_bytes(decrypted_block, iv)
        plain_text += block_xor
        iv = block
        cypher_text = cypher_text[16::1]
        block = cypher_text[0:16:1]
    return plain_text


port = 1200
block_size = 16
vector_initializare = b'1234567891234567'
k_prim = b'a doua cheie0000'
s = socket.socket()
s.bind(('', port))
s.listen(5)

s = socket.socket()
s.connect(('127.0.0.1', port))
encryption_key = s.recv(100)

op_mode = s.recv(100).decode()
print("Cheia " + str(encryption_key))
s.send("Communication start".encode())
crypt_text = s.recv(1000)
print("Am primit: " + str(crypt_text))
if op_mode == "ECB":
    print("plain text: " + unpad(decrypt_ecb(crypt_text, encryption_key), 16).decode())
elif op_mode == "CBC":
    print("plain text: " + unpad(decrypt_cbc(crypt_text, encryption_key, vector_initializare), 16).decode())
s.close()