exec(open("output.txt", "rb").read())
shared_key = y_A ** 2 * y_B ** 2 % p
flag  = c // shared_key
print(int.to_bytes(flag, (flag.bit_length() + 7) // 8, 'big'))
