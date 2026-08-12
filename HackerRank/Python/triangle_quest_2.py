#https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true

#using str solution
# if __name__ == '__main__':
#     for i in range(1, int(input()) + 1):
#         s = "".join([str(a) for a in range(1, i)]) + "".join([str(a) for a in range(i, 0, -1)])
#         print(s)

#more than one for statement solution
# if __name__ == '__main__':
#     for i in range(1, int(input()) + 1):
#         print(*(a for a in range(1,i)), *(a for a in range(i,0,-1)), sep="")


#shitty solution (what hackerrank wanted)
if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        print(((10**i)//9)**2)
