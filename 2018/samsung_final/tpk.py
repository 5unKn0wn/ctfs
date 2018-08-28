from Crypto.Cipher import CAST

key = "samsungctf_TPK\x00\x00"
iv = "aXZpc2hlcmU=".decode('base64')
enc = "5CE0B9F2C41C7D7368F7A5F69849BFE1CF5D82B259D14107607594EC3AD1352B1680D0C739F8B12812F96C78DEE49FBB".decode('hex')

cipher = CAST.new(key, CAST.MODE_OFB, iv)
print cipher.decrypt(enc)
