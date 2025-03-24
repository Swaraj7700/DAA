// modular a^b % n
#include<stdio.h>

int mod_exp(int a, int b, int n) {
    if(b == 1) return a % n;
    int half = mod_exp(a, b / 2, n);
    if(b % 2 == 0) return (half * half) % n;
    else return (half * half * (a % n)) % n;
}

int main() {
    int a = 7, b = 13, n = 15;
    printf("%d", mod_exp(a, b, n));
    return 0;
}