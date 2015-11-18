from event import EventDataValidator
import unittest


class MyTestCase(unittest.TestCase):
    def test_planned_donor_True(self):
        self.assertTrue(EventDataValidator.is_valid_planned_donor_number("100"))

    def test_planned_donor_False(self):
        self.assertFalse(EventDataValidator.is_valid_planned_donor_number("101"))

    def test_planned_donor_False2(self):
        self.assertFalse(EventDataValidator.is_valid_planned_donor_number("abc"))


if __name__ == '__main__':
    unittest.main()
