//https://www.hackerrank.com/challenges/reverse-array-c/problem?isFullScreen=true

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, * arr, i;
    scanf("%d", &num);
    arr = (int*)malloc(num * sizeof(int));
    for (i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    int* temparr = (int*)malloc(num * sizeof(int));
    for (int i = 0; i < num; i++) {
        temparr[num - 1 - i] = arr[i];
    }
    for (int i = 0; i < num; i++) {
        arr[i] = temparr[i];
    }



    for (i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}