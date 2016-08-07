#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int
main()
{
    int sock;
    struct sockaddr_in bindaddr;

    struct sockaddr_storage senderinfo;
    socklen_t addrlen;
    char buf[2048];
    int n;

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("socket");
        return 1;
    }

    bindaddr.sin_family = AF_INET;
    bindaddr.sin_port = htons(11112);
    bindaddr.sin_len = sizeof(bindaddr);

    if (bind(sock, (struct sockaddr *)&bindaddr, sizeof(bindaddr)) != 0) {
        perror("bind");
        return 1;
    }

    addrlen = sizeof(senderinfo);

    n = recvfrom(sock, buf, sizeof(buf) - 1, 0, (struct sockaddr *)&senderinfo, &addrlen);

    write(fileno(stdout), buf, n);
    sleep(1);
    write(fileno(stdout), buf, n);
    sleep(1);
    write(fileno(stdout), buf, n);
    sleep(1);
    write(fileno(stdout), buf, n);
    sleep(1);
    write(fileno(stdout), buf, n);
    sleep(1);
    write(fileno(stdout), buf, n);
    sleep(1);

    close(sock);

    return 0;
}
