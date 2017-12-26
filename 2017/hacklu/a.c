#include <stdio.h>

int main(void) {
	char a[0x100];
	scanf("%s", a);
	printf("%d\n", strlen(a));
	scanf("%s", a);
	printf("%d\n", strlen(a));
	printf("%d\n", strlen(a));
}
