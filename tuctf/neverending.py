from pwn import *

while True:
    r = remote("neverending.tuctf.com", 12345)

    r.sendlineafter("text:", "1234")
    r.recvuntil("is ")
    enc = r.recv(4)
    key = ord(enc[0]) - 0x31
    #log.info("enc : " + enc)
    #log.info("key : " + str(key))
    r.recvuntil("What is ")
    flag = r.recvuntil(" decrypted?\n:", drop=True)
    #log.info("flag : " + flag)
    send = ''.join(chr((ord(i) - key) & 0xff) for i in flag)
    print send
    #log.info("send : " + send)
    #for i in range(1000)
    r.send(send)
    r.interactive()
    r.close()
