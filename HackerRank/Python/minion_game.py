#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    substrings = []
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin += (length - i)
        else:
            stuart += (length - i)

    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart " + str(stuart))


if __name__ == '__main__':
    s = input()
    minion_game(s)