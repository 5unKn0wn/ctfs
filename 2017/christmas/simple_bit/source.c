#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int check(char *);
void shuffle(int *, int);
int main(void)
{
	char buf[256] = { 0, };
	int n;

	printf("Input : ");
	fflush(stdout);
	n = read(0, buf, sizeof(buf));
	buf[n - 1] = 0;

	if (check(buf)) {
		printf("Correct\n");
	}
	else {
		printf("Wrong\n");
	}

	return 0;
}

int check(char *input)
{
	int bin[256 * 8] = { 0, };
	int answer[256 * 8] = { 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, };
	int len = strlen(input);
	int diff = 1;

	for (int i = 0; i < len; i++) {
		for (int j = i * 8; j < i * 8 + 8; j++) {
			bin[j] = input[i] & 1;
			input[i] >>= 1;
		}
	}

	for (int i = 0; i < 16; i++) {
		diff = 1;
		for (int j = 0; j < len * 8; j++) {
			if (bin[j])
				diff ^= 1;
			bin[j] = diff;
		}
		shuffle(bin, len * 8);
	}

	for (int i = 0; i < 256 * 8; i++) {
		if (bin[i] != answer[i])
			return 0;
	}

	return 1;
}

void shuffle(int *input, int len)
{
	for (int i = len - 1; i >= 0; i--) {
		int n = rand() % len;
		if (i != n) {
			input[i] = input[i] ^ input[n];
			input[n] = input[i] ^ input[n];
			input[i] = input[i] ^ input[n];
		}
	}
}
