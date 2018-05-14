#!/usr/bin/make -f
CFLAGS=-O3
LDFLAGS=
LDLIBS=-lcrypto

all: pow

pow: pow.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o "$@" "$<" -lcrypto

clean:
	rm -f pow

.PHONY: all clean
