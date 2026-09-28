//https://www.hackerrank.com/challenges/functions-in-c/problem?isFullScreen=true

#include <stdio.h>
#include <math.h>

int max_of_four(int a, int b, int c, int d) {
    int maxnum = fmax(-1, a);
    maxnum = fmax(maxnum, b);
    maxnum = fmax(maxnum, c);
    return fmax(maxnum, d);

}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}