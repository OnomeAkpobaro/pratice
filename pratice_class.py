# class NegativeAge(Exception):
#     pass
# def set_age(age):
#     if age < 0:
#         raise NegativeAge("Age cannot be negative!")
#     print(f"Age is set to {age}")

# try:
#     set_age(-5)
# except NegativeAge as e:
#     print(e)


def add(a, b):
    return a + b

import unittest
class MathFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)

if __name__ == "__main__":
    unittest.main()