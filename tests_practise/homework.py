from typing import List, Dict, Union, Generator
import string
import math
import re


def task1(a, b):
    return list(set(a + b))


def task2(check_string):
        count = check_string.count("a")
        if count > 1:
            return count
        else:
            raise ValueError


def task3(num):
    if math.sqrt(num) == math.ceil(math.sqrt(num)):
        return math.sqrt(num)


def task4(num):
    while len(str(num)) != 1:
        num = sum([int(v) for v in str(num)])
    return num


def task5(mylist):
    mylist.append(0)
    del mylist[mylist.index(0)]
    return mylist


def task6(mylist2):
        l = [int(x) for x in list(mylist2)]
        diff = l[1] - l[0]
        for i in range(len(l) - 1):
            if not (l[i + 1] - l[i] == diff):
                return False
        return True


def task7(mylist3):
    a = ([str(x) for x in mylist3 if mylist3.count(x)==1])
    return int(a.pop(0))


def task8(mylist4):
    mylistnew = ([num for num in range(1, len(mylist4) + 2)])
    return int(''.join([str(x) for x in mylistnew if x not in mylist4]))


def task9(mylist5):
    return int(''.join([str(x) for x in range(len(mylist5)-1) if isinstance(mylist5[x], tuple)]))


def task10(string):
    return (''.join(reversed(string)))


def task11(min):
    h = 0
    while min / 60 >= 1:
        min -= 60
        h += 1
    return f"{h}:{min}"


def task12(string):
    string_new = re.sub('[!@#$&]', '', string)
    return max(string_new.split(), key=len)


def task13(string):
    string_new = reversed(string.split())
    return (' '.join(string_new))


def task14(n):
    def fibonacci(n):
        a, b = 1, 1
        for i in range(n):
            yield a
            a, b = b, a + b
    return list(fibonacci(n))


def task15(list):
    return([x for x in list if x%2 == 0])


def task16(n):
  #  n= int(input("n ="))
    if isinstance(n,int):
        return(sum([x+1 for x in range(0,(n))]))
    raise ValueError


def task17(n):
    a = 1
    for x in range(1, n+1):
        a *= x
    return a


def task18(list1):
    new_list = string.ascii_lowercase + 'a'
    list1 = [new_list[new_list.index(x) + 1] for x in list1]
    new_list = [x.upper() if x in ["a", "e", "i", "o", "u"] else x for x in list1]
    return ''.join(x for x in new_list)


def task19(string):
    string_new = re.sub('[!@#$&,.123456789]', '', string)
    return "".join(sorted(string_new))


def task20(n1, n2):
    if n1 > n2:
        return True
    elif n1 == n2:
        return "-1"
    return False


