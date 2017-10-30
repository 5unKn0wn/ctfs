def base64_decode(s):
    b64s = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210 /"
    b64p = "="
    ret = ""
    s2 = s.replace(b64p, "")
    left = 0
    for i in range(0, len(s2)):
        if left == 0:
            left = 6
        else:
            value1 = b64s.index(s2[i - 1]) & (2 ** left - 1)
            value2 = b64s.index(s2[i]) >> (left - 2)
            value = (value1 << (8 - left)) | value2
            ret += chr(value)
            left -= 2
    return ret

fake = "J9UFF9EWv9AABCEOHFEKAqUNNnVcIaM0"
secret_md5 = "5D8F988547D3B4087AE478403145ADC9"
resu = [0x4F, 0x38, 0x39, 0x79, 0x1B, 0x58, 0x3E, 0x28, 0x2D, 0x3A, 0x41, 0x08, 0x4A, 0x32, 0x1B, 0x0E, 0x14, 0x46, 0x46, 0x06, 0x05, 0x26, 0x58, 0x08, 0x2A, 0x1A, 0x5B, 0x10, 0x4E, 0x70, 0x37, 0x43]
encoded_base64 = ''.join(chr(ord(fake[i]) ^ ord(secret_md5[i]) ^ resu[i]) for i in range(len(fake)))[::-1]

print base64_decode(encoded_base64)
