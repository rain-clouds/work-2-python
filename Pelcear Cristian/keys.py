import random
import socket

from Crypto.Cipher import AES

k_prim = b'a doua cheie0000'
port = 1200
localhost='127.0.0.1'

def generate_and_crypt_key():
    key = ''.join([chr(random.randint(0, 0x7D)) for _ in range(16)])
    return AES.new(k_prim, AES.MODE_ECB).encrypt((bytes(key, encoding='utf8')))


s = socket.socket()
s.bind((localhost,port))
s.connect((localhost, port))

msg = s.recv(100).decode()
if msg == 'Send key':
    s.send(generate_and_crypt_key())

s.close()