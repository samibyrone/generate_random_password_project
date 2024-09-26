import unittest

from generate_password.random_password_generator import generate_password
from generate_password.random_password_generator import is_strong_password


class Generate_password(unittest.TestCase):

    def test_for_password(self):
        password = "SamsonIbironke"

    def test_that_generate_password_length_to_be_16_in_length(self):
        password = generate_password()
        self.assertEqual(len(password), 16, "Password should not be more than 16 characters long")

    def test_that_generate_password_that_contains_uppercase(self):
        password = generate_password()
        self.assertRegex(password, r".*[A-Z].*", "Password should contain at least minimum of one uppercase letter")

    def test_that_generate_password_that_contains_lowercase(self):
        password = generate_password()
        self.assertRegex(password, r".*[a-z].*", "Password should contain at least minimum of one lowercase letter")

    def test_that_password_is_strong_without_digit(self):
        password = "Abcdefghijklmno@"
        self.assertFalse(is_strong_password(password), "Password without digit should not be strong")

    def test_that_generate_password_that_contains_digit(self):
        password = generate_password()
        self.assertRegex(password, r".*\d.*", "Password should contain at least minimum of one digit")

    def test_that_generate_password_that_contains_special_characters(self):
        password = generate_password()
        self.assertRegex(password, ".*[@#$%^&*()-_+=<>?].*", "Password should contain at least minimum of one special character")

    def test_password_with_more_than_required_length(self):
        password = "Abcdefghijklmnop1@"
        self.assertTrue(is_strong_password(password), "Password longer than required length and should be strong")

    def test_password_with_lowercase(self):
        password = "abcdefghijklmno1@"
        self.assertFalse(is_strong_password(password), "Password without lowercase should not be strong")


