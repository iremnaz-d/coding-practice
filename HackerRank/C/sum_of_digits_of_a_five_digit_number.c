//https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem?isFullScreen=true

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d", &n);
    int first = n % 10;
    int second = (n % 100) / 10;
    int third = (n % 1000) / 100;
    int fourth = (n % 10000) / 1000;
    int fifth = n / 10000;
    printf("%d", first + second + third + fourth + fifth);
    return 0;
}