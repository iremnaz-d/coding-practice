#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    width = size * 2 - 1 + size * 2 - 2
    letters = []
    for i in range(1, size + 1):
        letters.append(chr(i + 96))

    for i in range(1,size+1):
        s = get_center(letters,i)
        print(s.center(width,"-"))

    for i in range(size-1,0,-1):
        s = get_center(letters, i)
        print(s.center(width, "-"))



def get_center(_list, length):
    size = len(_list)
    c_list = []
    counter = length-1
    i = size - 1
    while True:
        if counter >= 0:
            c_list.append(_list[i])
        else:
            current_length = len(c_list)-1
            for j in range(size-current_length , size):
                c_list.append(_list[j])
            break

        counter -= 1
        i -= 1


    return "-".join(c_list)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)