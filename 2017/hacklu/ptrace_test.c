#include <sys/ptrace.h>

int main(void) {
	printf("%x\n", ptrace(0, 0, 0, 0));
	printf("%x\n", ptrace(0, 0, 0, 0));
}
