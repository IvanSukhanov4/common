from typing import List, Dict, Union, Generator
import string
import math
import re


def task1(a, b):
    """
    Take two lists and write a program that returns a list that contains
    only the elements that are common between the lists (without duplicates).
    """
    return list(set(a + b))

def task2(check_string):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    """
    count = check_string.count("a")
    if count > 1:
        return count

def task3(num):
    """
    Write a Python program to check if a given positive integer is a power of three
    """
    return math.ceil(math.log(num, 3)) == math.floor(math.log(num, 3))

def task4(num):
    """
    Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit
    """
    while len(str(num)) != 1:
        num = sum([int(v) for v in str(num)])
    return num

def task5(mylist):
    """
    Write a Python program to push all zeros to the end of a list.
    """
    a = 0
    while 0 in mylist:
        mylist.pop(0)
        a += 1
    for b in range(a):
        mylist.append(0)
    return mylist

def task6(mylist2):
    """
    Write a Python program to check a sequence of numbers is an arithmetic progression or not
    """
    l = [int(x) for x in list(mylist2)]
    diff = l[1] - l[0]
    for i in range(len(l) - 1):
        if not (l[i + 1] - l[i] == diff):
            return False
    return True

def task7(mylist3):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    """
    a = ([str(x) for x in mylist3 if mylist3.count(x)==1])
    return int(a.pop(0))

def task8(mylist4):
    """
    Write a Python program to find a missing number from a list.
    """
    mylistnew = ([num for num in range(1, len(mylist4) + 2)])
    return int(''.join([str(x) for x in mylistnew if x not in mylist4]))

def task9(mylist5):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    """
    return int(''.join([str(x) for x in range(len(mylist5)-1) if isinstance(mylist5[x], tuple)]))

def task10(string):
    """
    Write a program that will take the str parameter being passed and return the string in reversed order.
    """
    return ''.join(reversed(string))

def task11(min):
    """
    Write a program that will take the num parameter being passed and return the number of hours and minutes the
    parameter converts to
    """
    h = 0
    while min / 60 >= 1:
        min -= 60
        h += 1
    return f"{h}:{min}"

def task12(string):
    """
    Write a program that will take the parameter being passed and return the largest word in the string
    """
    return max([re.sub("[^a-zA-Z]", "", word) for word in string.split()])

def task13(string):
    """
    Write a program that asks the user for a long string containing multiple words.
    Return the same string, except with the words in backwards order.
    """
    string_new = reversed(string.split())
    return ' '.join(string_new)

def task14(n):
    """
    Write a program that asks the user how many Fibonacci numbers to generate and then generates them
    """
    def fibonacci(n):
        a, b = 1, 1
        for i in range(n):
            yield a
            a, b = b, a + b
    return list(fibonacci(n))

def task15(list):
    """
    Write one line of Python that takes list and makes a new list that has only the even elements of this list in it
    """
    return([x for x in list if x%2 == 0])

def task16(n):
    """
    Write a program that will add up all the numbers from 1 to input number
    """
  #  n= int(input("n ="))
    if isinstance(n,int):
        return sum([x+1 for x in range(n)])
    raise ValueError

def task17(n):
    """
    Write a program that will take the parameter being passed and return the factorial of it
    """
    a = 1
    for x in range(1, n+1):
        a *= x
    return a

def task18(list1):
    """
    Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
    """
    new_list = string.ascii_lowercase + 'a'
    list1 = [new_list[new_list.index(x) + 1] for x in list1]
    new_list = [x.upper() if x in ["a", "e", "i", "o", "u"] else x for x in list1]
    return ''.join(x for x in new_list)

def task19(string):
    """
    Write a program that will take the str string parameter being passed and return the string with
    the letters in alphabetical order (ie. hello becomes ehllo)
    """
    string_new = re.sub('[!@#$&,.123456789]', '', string)
    return "".join(sorted(string_new))

def task20(n1, n2):
    """
    Write a program that will take both parameters being passed and return the true if num2 is greater than num1,
    otherwise return the false. If the parameter values are equal to each other then return the string -1
    """
    if n1 > n2:
        return True
    elif n1 == n2:
        return "-1"
    return False

