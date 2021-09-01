#include <arpa/inet.h>
#include <stdio.h>

int main() {
    struct in_addr{
        uint32_t s_addr;
    } * address;

    char* ip_address = "192.168.1.100";
    int res = inet_aton(ip_address, address);
    printf("res: %d\n : %d", res, address->s_addr);
    return 0;
}