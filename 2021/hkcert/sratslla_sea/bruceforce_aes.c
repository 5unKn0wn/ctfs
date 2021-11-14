#include <openssl/aes.h>
#include <stdio.h>

int main(void)
{
    unsigned char key[16] = "\x21\x63\x01\xb1\x9a\x5c\xc4\x66\xca\xdf\x94\xfc";
    unsigned char ct[] = "\x4f\x56\x91\xfa\x6f\x31\x45\xc4\xe1\x47\x0c\x5a\x9d\xf1\x99\xf7\x59\x0f\x4d\xfc\xbb\xa3\x5a\x98\xca\x97\xff\xd3\x2d\xd7\x1c\x8d\x17\x6a\x0d\xe6\xe5\x28\x00\xd0\x14\x80\xca\x9f\x79\xb3\xd6\x44\x66\x65\xf1\x8c\x1f\xf2\x0c\xbf\x23\xd6\x5b\xa6\xcf\x64\x38\x47";

    for (int a = 0; a < 256; a++) {
        key[12] = a;
        printf("%d\n", a);
        for (int b = 0; b < 256; b++) {
            key[13] = b;
            for (int c = 0; c < 256; c++) {
                key[14] = c;
                for (int d = 0; d < 256; d++) {
                    unsigned char pt[17] = { 0, };
                    key[15] = d;
                    AES_KEY aes_key;
                    AES_set_decrypt_key(key, 128, &aes_key);
                    AES_ecb_encrypt(ct, pt, &aes_key, AES_DECRYPT);
                    if (!memcmp(pt, "hkcert21{", 9)) {
                        printf("%s", pt);
                        AES_ecb_encrypt(ct + 16, pt, &aes_key, AES_DECRYPT);
                        printf("%s", pt);
                        AES_ecb_encrypt(ct + 32, pt, &aes_key, AES_DECRYPT);
                        printf("%s", pt);
                        AES_ecb_encrypt(ct + 48, pt, &aes_key, AES_DECRYPT);
                        printf("%s\n", pt);
                        return 0;
                    }
                }
            }
        }
    }
}
