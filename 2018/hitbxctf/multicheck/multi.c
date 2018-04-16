#include <stdio.h>

void decrypt (int* enc, unsigned int* table) {
    int sum=0xC6EF3720;
    unsigned int add_key=0x9e3779b9;
    for (int i = 0; i < 32; i++) {
        enc[1] -= ((enc[0]<<4) + table[2]) ^ (enc[0] + sum) ^ ((enc[0]>>5) + table[3]);
        enc[0] -= ((enc[1]<<4) + table[0]) ^ (enc[1] + sum) ^ ((enc[1]>>5) + table[1]);
        sum -= add_key;
    }
}

int main(void) {
	int enc[5][2] = {{0x637c65e9, 0x8e51d1d9}, {0x9a4f1634, 0xd9a2beb8}, {0x65ee49e5, 0x35fb2eec}, {0x610bc824, 0xedcf90b5}};
	unsigned int table[4] = {0xabababab, 0xcdcdcdcd, 0xefefefef, 0x12345678};
    char flag[28] = { 0 };

	for (int i = 0; i < 5; i++) 
        decrypt(enc[i], table);

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 2; j++) {
            if (i == 0)
                j = 1;
            for (int k = 3; k >= 0; k--) {
                printf("%c", (enc[i][j] >> (8 * k)) & 0xff);
            }
        }
    }
}
