import unittest
from Serial import SerialWithErrorsProtection


class TestDataValidation(unittest.TestCase):

    def test_empty_data(self):
        data = ""
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), False)

    def test_not_numbers(self):
        data = "abc"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), False)

    def test_not_only_numbers1(self):
        data = "-123.321 abc"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), False)

    def test_not_only_numbers2(self):
        data = "-123.321 1 2 3 abc ;36"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), False)

    def test_only_doubles(self):
        data = "-123.321 888.800"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), False)

    def test_correct_data(self):
        data = "-123.321 888.800 1 2 3 -4 38 40"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), True)
        self.assertEqual(SerialWithErrorsProtection.parse_data(data), (-123.321, 888.800, [1, 2, 3, -4, 38, 40]))


    def test_(self):
        data = "-123.321 888.800 38468"
        # print(data)
        self.assertEqual(SerialWithErrorsProtection.validate_data(data), True)
        self.assertEqual(SerialWithErrorsProtection.parse_data(data), (-123.321, 888.800, [38468]))


if __name__ == '__main__':
    unittest.main()