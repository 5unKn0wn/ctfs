#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct user {
	char color[8];
	char name[8];
	void (*next)(struct user*);
};

void chomp(char *str) {
	ssize_t last = strlen(str) - 1;
	if (last >= 0 && str[last] == '\n')
		str[last] = '\0';
}

void dead(struct user *user) {
	printf("%s: Auuuuuuuugh!\n", user->name);
	user->next = NULL;
}

void success_knight(struct user *user) {
	printf("Keeper: Right. Off you go.\n");
	user->next = NULL;
}

void success_king(struct user *user) {
	printf("Keeper: What? I don't know that! Auuuuuuuugh!\n");
	printf("FLAG\n");
	user->next = NULL;
}

void check_knight(struct user *user) {
	user->next = success_knight;
	printf("Keeper: What is your favorite color?\n");
	char *res = fgets(user->color, sizeof(struct user), stdin);
	if (res == NULL) {
		user->next = NULL;
		return;
	}
	chomp(user->color);
	if (strcmp(user->color,"red")) {
		user->next = dead;
	}
}

void check_king(struct user *user) {
	user->next = success_king;
	printf("Keeper: What is the air-speed velocity of an unladen swallow?\n");
	printf("%s: What do you mean?\n", user->name);
	char *res = fgets(user->color, sizeof(struct user), stdin);
	if (res == NULL) {
		user->next = NULL;
		return;
	}
	chomp(user->color);
	user->next = success_king;
	if (strcmp(user->color,"An African or European swallow?")) {
		user->next = dead;
	}
}

void start(struct user *user) {
	printf("Keeper: Stop! What is your name?\n");
	char *res = fgets(user->name, sizeof(struct user), stdin);
	if (res == NULL) {
		user->next = NULL;
		return;
	}
	chomp(user->name);

	size_t len = strlen(user->name);
	if (len < 2) {
		printf("Keeper: Sorry `%s', your name is too short\n", user->name);
		user->next = NULL;
		return;
	}

	if(!strncmp(user->name, "Arthur", 6)) {
		user->next = check_king;
		printf("Arthur: It is Arthur, King of the Britons.\n");
	} else {
		user->next = check_knight;
		printf("%s: Sir %s of Camelot.\n", user->name, user->name);
	}
}

int main(void) {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);

	struct user *user = malloc(sizeof(struct user));
	user->next = start;
	while(user->next) user->next(user);
	return 0;
}
