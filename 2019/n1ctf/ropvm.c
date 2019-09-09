#include <stdio.h>

void decipher(unsigned int num_rounds, unsigned int v[2], unsigned int const key[4]) {
    unsigned int i;
    unsigned int v0=v[0], v1=v[1], delta=0x5F3759DF, sum=delta*num_rounds;
    for (i=0; i < num_rounds; i++) {
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
        sum -= delta;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
    }
    v[0]=v0; v[1]=v1;
}

int main(void)
{
	unsigned int v[][2] = { { 0x86dab2be, 0x146d16a8 }, { 0x3c9edb52, 0x54f1658f }, { 0x19c12643, 0x2a33699d }, { 0xcd9e6b, 0xc1ce3226 } };
	unsigned int key[] = {0x67343146, 0x34313146, 0x31314667, 0x67343131};
	unsigned int flag[9] = { 0 };
	
	for (int i = 0; i < 4; i++) {
		decipher(32, v[i], key);
		flag[i * 2 + 0] = v[i][0];
		flag[i * 2 + 1] = v[i][1];
	}
	
	printf("%s", (char*)flag);

	return 0;
}