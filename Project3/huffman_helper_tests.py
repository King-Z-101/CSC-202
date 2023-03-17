import unittest
from huffman import *


class TestHuffmanHelper(unittest.TestCase):
    def test_create_code_helper(self):
        # Test with infile.txt
        freq_list = cnt_freq("in_file.txt")
        huff_tree_root = create_huff_tree(freq_list)
        huff_codes = create_code(huff_tree_root)
        self.assertEqual(huff_codes[ord('e')], '1')
        self.assertEqual(huff_codes[ord('b')], '00')
        self.assertEqual(huff_codes[ord('d')], '01')
        self.assertEqual(create_code_helper(huff_tree_root, "", [""] * 256), True)

        # Test with infile3.txt (huffman example)
        freq_list3 = cnt_freq("in_file_3.txt")
        huff_tree_root3 = create_huff_tree(freq_list3)
        huff_codes3 = create_code(huff_tree_root3)
        self.assertEqual(huff_codes3[ord(' ')], '00')
        self.assertEqual(huff_codes3[ord('b')], '01')
        self.assertEqual(huff_codes3[ord('d')], '100')
        self.assertEqual(huff_codes3[ord('c')], '101')
        self.assertEqual(huff_codes3[ord('a')], '11')
        self.assertEqual(create_code_helper(huff_tree_root3, "", [""] * 256), True)


if __name__ == "__main__":
    unittest.main()
