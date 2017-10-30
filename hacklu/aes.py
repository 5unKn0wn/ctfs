from Crypto.Cipher import AES
import binascii
import os

# key = '\xBF\xE3\x80\x6E\x8C\xB7\x0A\x4E\x6E\x96\x00\x63\x88\x00\x09\x9E'
key = 'E1607975323C7317FFCAD91E3E396ABC'.decode('hex')
key = '78756C46466C757878756C461E190D21'.decode('hex')
IV = '\x00' * 0x10
encryptor = AES.new(key, AES.MODE_CBC, IV = IV)
# text = '356F21DEF7BD78FE6DB13CC6BC499CA9'.decode('hex')
text = '7B4D6FF46AC46C3F628ACC930D937D81'.decode('hex')
text = 'E1607975323C7317FFCAD91E3E396ABC'.decode('hex')
plaintext = encryptor.decrypt(text)
print plaintext
