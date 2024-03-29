import unittest

from string_calculator import add

# Unit testing of string calculator
class TestStringCalculator(unittest.TestCase):

  def test_empty_string(self):
    self.assertEqual(add(""), 0)

  def test_comma(self):
    self.assertEqual(add("1"), 1)
    self.assertEqual(add("1,2"), 3)

  def test_newlines(self):
    self.assertEqual(add("1\n2,3"), 6)
    self.assertRaises(ValueError, add, "1,\n")

  def test_delimeter(self):
    self.assertEqual(add("//;\n1;2;3;4"), 10)
    self.assertEqual(add("//*\n1*2*3*4"), 10)
    self.assertRaises(ValueError, add, "//*\n1*\n")

  def test_negatives(self):
    self.assertRaises(ValueError, add ,"1,-2")

    try:
      add("1,-2,3")
    except ValueError as e:
      self.assertEqual(str(e), 'negatives not allowed. found -2')

unittest.main()
