//https://www.hackerrank.com/challenges/bitwise-operators-in-c/problem?isFullScreen=true

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
    int maxand = 0, maxor = 0, maxxor = 0;

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i != j) {
                int and = i & j;
                if (and > maxand && and < k) maxand = and;

                int or = i | j;
                if (or > maxor && or < k) maxor = or ;

                int xor = i ^ j;
                if (xor > maxxor && xor < k) maxxor = xor;
            }
        }
    }

    printf("%d\n%d\n%d", maxand, maxor, maxxor);
}

int main() {
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}
