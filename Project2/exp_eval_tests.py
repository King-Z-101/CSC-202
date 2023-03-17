import unittest
from exp_eval import *


class TestProject2(unittest.TestCase):
    def test_infixToPostfix(self):
        self.assertEqual(infix_to_postfix("1 * 2 + 3 * 4"), "1 2 * 3 4 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3 - ( 4 - 5 ) * ( 6 + 7 )"), "1 2 + 3 * 4 5 - 6 7 + * -")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("3 * ( 4 + 5 ) / 6"), "3 4 5 + * 6 /")
        self.assertEqual(infix_to_postfix("( 2 + 3 ) * 4"), "2 3 + 4 *")
        self.assertEqual(infix_to_postfix('2.5 + 3.2 * 4 / ( 5.2 - 6.1 )'), '2.5 3.2 4 * 5.2 6.1 - / +')
        self.assertEqual(infix_to_postfix('( 3 + 4 ) * ( 5 - 6 )'), '3 4 + 5 6 - *')
        self.assertEqual(infix_to_postfix('( 2 + 3.8 ) * 4.2 - 5.1 / 6.2 ** 7.3'), '2 3.8 + 4.2 * 5.1 6.2 7.3 ** / -')

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("6 4 3 + 5 - ** 6 /"), 6)
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        self.assertEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertEqual(postfix_eval("4 2 / 3 +"), 5)
        self.assertEqual(postfix_eval("5.5 2.5 * 1.5 /"), 9.17)
        self.assertEqual(postfix_eval("5 2 <<"), 20)
        self.assertEqual(postfix_eval("10 3 >>"), 1)
        with self.assertRaises(ValueError):
            postfix_eval("3 2 + 0 /")
        with self.assertRaises(PostfixFormatException):
            postfix_eval("")
            postfix_eval('')
            postfix_eval("     ")
            postfix_eval("3 / 2 >>")
            postfix_eval("3 3 / 1 >>")
            #Too many operands
            postfix_eval("33 3")
            postfix_eval("1 2 3 +")
            # Insufficient Operands
            postfix_eval("33 3 / * +")
            postfix_eval("4 +")
            # Not a valid operator or operand
            postfix_eval("blah")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6 "), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* + 1 2 3"), "1 2 + 3 *")
        self.assertEqual(prefix_to_postfix("- / 10 5 + 6 4"), "10 5 / 6 4 + -")
        self.assertEqual(prefix_to_postfix("/ * 10 + 2 3 5"), "10 2 3 + * 5 /")
        self.assertEqual(prefix_to_postfix(">> 6 2"), "6 2 >>")
        self.assertEqual(prefix_to_postfix("* + 3 4 - 5 -6"), '3 4 + 5 -6 - *')
        self.assertEqual(prefix_to_postfix("+ 2.5 / * 3.2 4.6 - 5.2 6.1 "), "2.5 3.2 4.6 * 5.2 6.1 - / +")
        self.assertEqual(prefix_to_postfix('- * + 2.7 3.8 4.2 / 5.1 **  6.2 7.3'), '2.7 3.8 + 4.2 * 5.1 6.2 7.3 ** / -')


if __name__ == "__main__":
    unittest.main()

