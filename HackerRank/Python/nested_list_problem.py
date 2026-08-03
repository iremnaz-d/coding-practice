#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':

    _list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        _list.append([name, score])

    _list.sort(reverse=False, key=lambda g: g[1])

    s_list = []
    first_grade = _list[0][1]
    second_grade = 0

    for i in _list:
        if i[1] != first_grade:
            second_grade = i[1]
            break

    for i in _list:
        if i[1] == second_grade:
            s_list.append(i)
    s_list.sort(reverse=False, key=lambda x: x[0])

    for i in s_list:
        print(i[0])



