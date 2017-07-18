#include <stdio.h>

int main(void) {
	int fd = open("flag", 0x41, 0x1A4);
	printf("%d\n", fd);

	write(fd, "my_value", 8);
	write(fd, "sexsex", 6);

	close(fd);
}
