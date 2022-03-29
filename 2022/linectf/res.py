from Crypto.Cipher import AES, DES3, ARC4
from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives.ciphers import algorithms, base, modes
 
import itertools
import camellia
import base64
 
def decrypt_rc4(ct):
    key = b'G\x06H\x08Q\xe6\x1b\xe8]t\xbf\xb3\xfd\x95a\x85'
  
    rc4 = ARC4.new(key)
    return rc4.decrypt(ct)
 
def decrypt_aes(ct):
    key = b'\xa7A\xbe\x141\xdd\x82IcW\xba\xf11\xae\xcf\xd5'
    iv = b'\xc9\x19(\xc8O\xc6\x1b\xe8]y\xcf\x83\xfd\x95\xc1\x85'
 
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(ct)
 
def decrypt_3des(ct):
    key = b'HELPME!\x00THANKS!\x00\x10\x20\x30\x40\x50\x60\x70\x80'
 
    des3 = DES3.new(key, DES3.MODE_ECB)
    return des3.decrypt(ct)
 
def decrypt_camellia(ct):
    key = b'\x11"3DUfw\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00'
 
    camel = camellia.CamelliaCipher(key=key, mode=camellia.MODE_ECB)
    return camel.decrypt(ct)
 
def decrypt_seed(ct):
    key = b'\xff\x04(a!\xea\x1b\xe8mq\xcc\xb1\xfd\xa7C\x82'
 
    mode = modes.ECB()
    cipher = base.Cipher(algorithms.SEED(key), mode, backend)
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct)
    pt += decryptor.finalize()
    return pt
 
funcs = [decrypt_rc4, decrypt_aes, decrypt_3des, decrypt_camellia, decrypt_seed]
 
ct = "N9Nb2sPYFl6sEbVORzuK1kUXMvs+/LbyrTpJaxQj3fdDhXyKN8mBELPRTX5904o9"
ct = base64.b64decode(ct)
 
for order in itertools.permutations(range(5), 5):
    pt = funcs[order[0]](ct)
    pt = funcs[order[1]](pt)
    pt = funcs[order[2]](pt)
    pt = funcs[order[3]](pt)
    pt = funcs[order[4]](pt)
    if b"LINECTF" in pt:
        print(pt)
        break
