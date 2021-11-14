from sha256 import SHA256
from pwn import *
import hashlib
import base64

def work():
    r.recvuntil("🔧 ")
    challenge = base64.b64decode(r.recvline())
    print(challenge)
    answer = 1
    while True:
        if answer % 1000000 == 0:
            print(answer)
        answer_str = int.to_bytes(answer, (answer.bit_length() + 7) // 8, 'big')
        if hashlib.sha256(challenge + answer_str).digest().startswith(b'\x00\x00\x00'):
            print(f"Found answer: {answer_str}")
            r.sendlineafter("🔩 ", base64.b64encode(answer_str))
            return
        answer += 1

def spy(pbox, salt):
    r.sendlineafter("🤖 ", "🕵️")
    r.sendlineafter("😵 ", str(pbox))
    r.sendlineafter("🧂 ", base64.b64encode(salt))
    r.recvuntil("🔑 ")
    return bytes.fromhex(r.recvline().decode())

def auth(password):
    r.sendlineafter("🤖 ", "🖥️")
    r.recvuntil("😵 ")
    pbox = eval(r.recvline())
    r.recvuntil("🧂 ")
    salt = base64.b64decode(r.recvline())

    permutated_password = password + salt + b"\x00"
    permutated_password = bytes([permutated_password[pbox[i]] for i in range(21)])
    hashed_password = hashlib.sha256(permutated_password).hexdigest()
    r.sendlineafter('🔑 ', hashed_password)


while True:
    r = remote("chalp.hkcert21.pwnable.hk", 28167, level='error')

    work()
    
    h_target = spy(list(range(21)), b'\x00\x00\x00\x00')

    charset = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    mapper = {}
    for c in charset:
        for pepper in range(256):
            s = SHA256(h_target)
            s.feed(bytes([c, pepper]) + b'\x80' + b'\x00' * 59 + b'\x02\x10')
            h = s.digest()
            mapper[h] = bytes([c])
    print("Mapping ends")

    password = b''
    for i in range(33):
        # sucess if first pepper is {i}
        for j in range(16):
            #                password      salt                   pepper 0x80     null          bits  c  pepper
            h_sub = spy(list(range(16)) + [0x11, 0x11, 0x11, 0x11, 0x10, 0x12] + [0x11] * 41 + [0x13, j, 0x14], f'{chr(i)}\x00\x80\xa8'.encode('latin-1'))
            c = mapper.get(h_sub)
            if c == None:
                break
            password += c

        if password != b'':
            print(f"Found password: {password}")
            break

    if password == b'':
        print("failed...")
        r.close()
        continue

    auth(password)
    r.interactive()
