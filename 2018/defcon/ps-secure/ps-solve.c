// clang -o ps-solve ps-solve.c -O3 -lcrypto
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <openssl/md5.h>

static inline void asciz_to_md5hex(const void *ptr, size_t len, char *out)
{
    unsigned char md[16];
    unsigned int i;

    MD5(ptr, len, md);
    for (i = 0; i < 16; i++)
    {
        unsigned char vhi = md[i] >> 4,
                  vlo = md[i] & 0xf;
        out[i*2+0] = vhi >= 0xa ? vhi + ('a' - 0xa) : vhi + '0';
        out[i*2+1] = vlo >= 0xa ? vlo + ('a' - 0xa) : vlo + '0';
    }
}

static inline void hex32(char *out, uint32_t val)
{
    unsigned int i;

    for (i = 0; i < 8; i++)
    {
        unsigned char nib;
        nib = (val >> (28 - i * 4)) & 0xfu;
        *out++ = nib >= 0xa ? nib + ('a' - 0xa) : nib + '0';
    }
}

#define MY_RAND(x) ((((x) = 0x343FDu * (x) + 0x269EC3) >> 16) & 0x7FFFu)

int main (int argc, char **argv)
{
    uint32_t seed = 0x374b2e90;
    char buf[100] = "c5de4d2384b161f87e6f79adff0e1d56";	// md5 of noise
    unsigned int i;

    asciz_to_md5hex(buf, 32, buf);
    buf[32] = '-';
    hex32(&buf[32 + 1], MY_RAND(seed));
    for (i = 0; i < 99999999; i++)
    {
        asciz_to_md5hex(buf, 32 + 1 + 8, buf);
	buf[32] = '-';
        hex32(&buf[32 + 1], MY_RAND(seed));
    }
    // Flag:{5fddb416617b9e2cd2dcc359917d851b-0000202a}
    printf("Flag:{%.41s}\n", buf);
    return 0;
}
