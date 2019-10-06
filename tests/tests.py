import unittest
from homework import Rectangle
from math import sqrt


class Test(unittest.TestCase):

    def setUp(self):
        self.width = 4
        self.height = 5
        self.rect = Rectangle(self.width, self.height)


    def test_get_rectangle_perimeter(self):
        in_process = self.rect.get_rectangle_perimeter()
        in_result = ((self.width + self.height)*2)
        self.assertEqual(in_process, in_result)


    def test_get_rectangle_square(self):
        in_process = self.rect.get_rectangle_square()
        in_result = self.width * self.height
        self.assertEqual(in_process, in_result)


    def test_get_sum_of_corners(self):
        in_result = 90 * 3
        in_process = self.rect.get_sum_of_corners(3)
        self.assertEqual(in_process, in_result)


    def test_get_rectangle_diagonal(self):
        in_process = self.rect.get_rectangle_diagonal()
        in_result = sqrt(4 ** 2 + 5 ** 2)
        self.assertEqual(in_process, in_result)


    def test_get_radius_of_circumscribed_circle(self):
        in_process = self.rect.get_radius_of_circumscribed_circle()
        in_result = (sqrt(4 ** 2 + 5 ** 2))/2
        self.assertEqual(in_process, in_result)


    def test_radius_of_inscribed_circle(self):
        in_process = Rectangle(8, 8).get_radius_of_inscribed_circle()
        in_result = (8/2)
        self.assertEqual(in_process, in_result)
#Errors

    def test_get_sum_of_corners_ValueError(self):
        with self.assertRaises(ValueError):
            self.rect.get_sum_of_corners(5 or 0)


    def test_radius_of_inscribed_circle_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(8,9).get_radius_of_inscribed_circle()





if __name__ == "__main__":
    unittest.main()