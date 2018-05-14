#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <inttypes.h>
#include <openssl/sha.h>

static int solve_chall(const void *chall, size_t chall_len, unsigned char bits, uint64_t *res, uint64_t start, uint64_t end)
{
    uint8_t message[64] = { 0u }, *wptr;
    const uint_fast8_t q = bits - 1, w = 7 - (q >> 5), k = 31 - (q & 31);
    uint64_t value;
    if (chall_len > 47 || bits > 32) return -1;
    else if (bits < 1)
    {
        *res = start;
        return 0;
    }
    memcpy(message, chall, chall_len);
    message[chall_len + 8] = 0x80;
    message[62] = (chall_len + 8) >> 5;
    message[63] = (chall_len + 8) << 3;
    value = start;
    wptr = message + chall_len;
    do
    {
        SHA256_CTX ctx;
        uint_fast8_t bi;
        memset(&ctx, 0, sizeof(SHA256_CTX));
        ctx.h[0] = 0x6a09e667UL;
        ctx.h[1] = 0xbb67ae85UL;
        ctx.h[2] = 0x3c6ef372UL;
        ctx.h[3] = 0xa54ff53aUL;
        ctx.h[4] = 0x510e527fUL;
        ctx.h[5] = 0x9b05688cUL;
        ctx.h[6] = 0x1f83d9abUL;
        ctx.h[7] = 0x5be0cd19UL;
        ctx.md_len = SHA256_DIGEST_LENGTH;
        wptr[0] = (value & 0xffu),
            wptr[1] = ((value >> 8) & 0xffu),
            wptr[2] = ((value >> 16) & 0xffu),
            wptr[3] = ((value >> 24) & 0xffu),
            wptr[4] = ((value >> 32) & 0xffu),
            wptr[5] = ((value >> 40) & 0xffu),
            wptr[6] = ((value >> 48) & 0xffu),
            wptr[7] = ((value >> 56) & 0xffu);
        SHA256_Transform(&ctx, (const unsigned char *) message);
        for (bi = 7; ; --bi)
        {
            if (bi == w)
            {
                if ((ctx.h[w] << k) == 0)
                {
#if 0
                    int i;
                    for (i = 0; i < 64; i++)
                        fprintf(stderr, "%02x", message[i]);
                    fputc('\n', stderr);
                    for (i = 0; i < 8; i++)
                        fprintf(stderr, "%08x", ctx.h[i]);
                    fputc('\n', stderr);
#endif
                    *res = value;
                    return 0;
                }
                break;
            }
            else if (ctx.h[bi] != 0)
                break;
        }
    } while (end != ++value);
    return -1;
}

int main(int argc, char* argv[])
{
    /* empty message with padding */
    long bits;
    uint64_t val = 0;
    int res;

    if (argc != 3) return EXIT_FAILURE;
    bits = strtol(argv[2], NULL, 0);
    if (bits < 0 || bits > 32) return EXIT_FAILURE;
    res = solve_chall(argv[1], strlen(argv[1]), (unsigned char) bits, &val, 0, 0);
    if (res < 0)
        return EXIT_FAILURE;
    printf("%" PRIu64 "\n", val);
    return EXIT_SUCCESS;
}
