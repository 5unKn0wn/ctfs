from itertools import product
import struct

key_list = [["andro", "linux"], [1], [0, 1], [0, 1], [0, 1], [0, 1], ["af", "sq", "ar", "eu", "bg", "be", "ca", "zh", "hr", "cs", "da", "nl", "en", "et", "fo", "fa", "fi", "fr", "gd", "de", "el", "he", "hi", "hu",  "is", "id", "it", "ja", "ko", "lv", "lt", "mk", "mt", "no", "pl", "pt", "rm", "ro", "ru", "sz", "sr", "sk", "sl", "sb", "es", "sx", "sv", "th", "ts", "tn", "tr", "uk", "ur", "ve", "vi", "xh", "ji", "zu"], [0, 1], [0, 1], [0, 1], [0, 1]]

for l in product(*key_list):
	enc = "A2xcVTrDuF+EqdD8VibVZIWY2k334hwWPsIzgPgmHSapj+zeDlPqH/RHlpVCitdlxQQfzOjO01xCW/6TNqkciPRbOZsizdYNf5eEOgghG0YhmIplCBLhGdxmnvsIT/69I08I/ZvIxkWyufhLayTDzFeGZlPQfjqtY8Wr59Lkw/JggztpJYPWng==".decode('base64')
	enc = list(struct.unpack("<" + "L" * 34, enc))
	key = ''.join(str(i).upper() for i in l)
	key = list(struct.unpack("<LLLL", key[:16]))

	k = 0x9e3779b9 * 7
	while k:
		d = 3 & (k >> 2)
		for i in range(len(enc) - 1, -1, -1):
			enc[i] -= ((enc[i - 1] >> 5) ^ (enc[(i + 1) % len(enc)] << 2)) + (enc[(i + 1) % len(enc)] >> 3 ^ enc[i - 1] << 4) ^ (k ^ enc[(i + 1) % len(enc)]) + (key[3 & i ^ (3 & k >> 2)] ^ enc[i - 1])
			enc[i] &= 0xffffffff
		k -= 0x9e3779b9

	r = struct.pack("<" + "L" * 34, *enc)
	if "var" in r:
		print r
		break
