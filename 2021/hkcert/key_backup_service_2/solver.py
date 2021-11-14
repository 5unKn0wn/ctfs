from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from tqdm import tqdm
from math import gcd
import pickle

f = open("transcript.log", "r")
ns = []
cs = []

enc_2 = 2 ** 65537
enc_3 = 3 ** 65537
gcd_args = []
l = []
while True:
    line = f.readline()
    if line == '':
        break
    command, option, *args = line.strip().split(' ')
    if option == "flag":
        flag_ct = bytes.fromhex(f.readline())
    elif option == "pkey":
        pass
    elif option == "send":
        if args[0] == '2':
            c2 = int(f.readline(), 16)
            gcd_args.append(enc_2 - c2)
        elif args[0] == '3':
            c3 = int(f.readline(), 16)
            gcd_args.append(enc_3 - c3)
            ns.append(gcd(*gcd_args))
            assert pow(2, 65537, ns[-1]) == c2
            assert pow(3, 65537, ns[-1]) == c3
            gcd_args = []
    elif option == "backup":
        cs.append(int(f.readline(), 16))
    else:
        raise Exception(option)
print("Recovering all modulus/ciphertext done")

# 7265 11437
for i in range(len(ns)):
    for j in range(i + 1, len(ns)):
        if gcd(ns[i], ns[j]) > 2**100:
            print(i, j)
            p = gcd(ns[i], ns[j])
            q = ns[j] // p
            d = pow(65537, -1, (p - 1) * (q - 1))
            master_secret = int.to_bytes(pow(cs[j], d, ns[j]), 32, 'big')
            print(unpad(AES.new(master_secret, AES.MODE_CBC, b'\x00' * 16).decrypt(flag_ct), 16))
            exit()
