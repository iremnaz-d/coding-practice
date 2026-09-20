//https://www.hackerrank.com/challenges/playing-with-characters/problem?isFullScreen=true

#include <stdio.h>


int main()
{
    char ch;
    char s[100];
    char sen[100];

    scanf("%c", &ch);
    scanf("%s", &s);
    scanf("\n");
    scanf("%[^\n]%*s", &sen);

    printf("%c\n%s\n%s", ch, s, sen);

    return 0;
}