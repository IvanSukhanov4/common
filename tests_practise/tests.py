import unittest
from homework import (task1, task2, task3, task4,
                      task5, task6, task7, task8,
                      task9, task10, task11, task12,
                      task13, task14, task15, task16,
                      task17, task18, task19, task20)


class Test(unittest.TestCase):


    def test_task1(self):
        a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        in_process = task1(a, b)
        in_results = [1, 2, 3, 34, 5, 4, 6, 8, 7, 9, 10, 11, 13, 12, 21, 55, 89]
        self.assertEqual(in_process, in_results)

    def test_task2(self):
        check_string = ' I am a good developer. I am also a writer '
        in_process = task2(check_string)
        in_results = 5
        self.assertEqual(in_process, in_results)

    def test_task3(self):
        in_results = 3
        self.assertTrue(task3(81))

    def test_task4(self):
        in_process = task4(59)
        in_results = 5
        self.assertEqual(in_process, in_results)

    def test_task5(self):
        mylist = [0,2,3,4,6,7,10]
        in_process = task5(mylist)
        in_results = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(in_process, in_results)

    def test_task6(self):
        mylist2 = [5, 7, 9, 11]
        self.assertTrue(task6([5, 7, 9, 11]))

    def test_task7(self):
        mylist3 = [5, 3, 4, 3, 4]
        in_process = task7(mylist3)
        in_results = 5
        self.assertEqual(in_process, in_results)

    def test_task8(self):
        mylist4 =  [1,2,3,4,6,7,8]
        in_process = task8(mylist4)
        in_results = 5
        self.assertEqual(in_process, in_results)

    def test_task9(self):
        mylist5 = [1,2,3,4,(1,2),3]
        in_process = task9(mylist5)
        in_results = 4
        self.assertEqual(in_process, in_results)

    def test_task10(self):
        string = "Hello World and Coders"
        in_process = task10(string)
        in_results = "sredoC dna dlroW olleH"
        self.assertEqual(in_process, in_results)

    def test_task11(self):
        min = 60
        in_process = task11(min)
        in_results = "1:0"
        self.assertEqual(in_process, in_results)

    def test_task12(self):
        string = "fun&!! time"
        in_process = task12(string)
        in_results = "time"
        self.assertEqual(in_process, in_results)
        self.assertEqual(task12("I love dogs"), "love")

    def test_task13(self):
        string = "My name is Michele"
        in_process = task13(string)
        in_results = "Michele is name My"
        self.assertEqual(in_process, in_results)

    def test_task14(self):
        n = 10
        in_process = task14(n)
        in_results = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(in_process, in_results)

    def test_task15(self):
        list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        in_process = task15(list)
        in_results = [4, 16, 36, 64, 100]
        self.assertEqual(in_process, in_results)

    def test_task16(self):
        n = 4
        in_process = task16(n)
        in_results = 10
        self.assertEqual(in_process, in_results)

    def test_task16_ValueError(self):
        self.assertRaises(ValueError, task16, "ajj")

    def test_task17(self):
        n = 4
        in_process = task17(n)
        in_results = 24
        self.assertEqual(in_process, in_results)

    def test_task18(self):
        self.assertEqual(task18("abcd"), "bcdE")

    def test_task19(self):
        string = "e1234&,.dcba"
        in_process = task19(string)
        in_results = "abcde"
        self.assertEqual(in_process, in_results)

    def test_task20(self):
        self.assertTrue(task20(57, 21))
        self.assertEqual(task20(4, 4), '-1')
        self.assertFalse(task20(122, 398))


if __name__ == "__main__":
    unittest.main()
