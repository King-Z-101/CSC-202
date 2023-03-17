import unittest

import huffman
from huffman import *


class TestHuffman(unittest.TestCase):
    def test_cnt_freq(self):
        #Test with in_file.txt
        freq_list = cnt_freq("in_file.txt")
        char_list = [0] * 256
        char_list[97:100] = [0, 1, 0, 1, 2]
        self.assertListEqual(freq_list[97:100], char_list[97:100])

        #Test with in_file_2.txt
        freq_list2 = cnt_freq("in_file_2.txt")
        char_list2 = [0] * 256
        char_list2[97:100] = [4, 2, 0, 4]
        self.assertListEqual(freq_list2[97:100], char_list2[97:100])

        #test with huffman example (infile3.txt)
        freqList10 = cnt_freq("in_file_3.txt")
        char_list10 = [0] * 256
        char_list10[32:33] = [3, 0]
        self.assertListEqual(freqList10[32:33], char_list10[32:33])
        char_list10[97:100] = [4, 3, 2, 1]
        self.assertListEqual(freqList10[97:100], char_list10[97:100])

    def test_create_huff_tree(self):
        # Test with in_file.txt
        freq_list = cnt_freq("in_file.txt")
        huff_tree_root = create_huff_tree(freq_list)
        self.assertEqual(huff_tree_root.char, "b")
        self.assertEqual(huff_tree_root.count, 4)

        # Test with in_file_2.txt
        freq_list2 = cnt_freq("in_file_2.txt")
        huff_tree_root2 = create_huff_tree(freq_list2)
        self.assertEqual(huff_tree_root2.char, "a")
        self.assertEqual(huff_tree_root2.count, 10)

        #Test with huffman_example (infile3.txt)
        freq_list3 = cnt_freq("in_file_3.txt")
        huff_tree_root3 = create_huff_tree(freq_list3)
        self.assertEqual(huff_tree_root3.char, " ")
        self.assertEqual(huff_tree_root3.count, 13)


    def test_create_code(self):
        #Test with infile.txt
        freq_list = cnt_freq("in_file.txt")
        huff_tree_root = create_huff_tree(freq_list)
        huff_codes = create_code(huff_tree_root)
        self.assertEqual(huff_codes[ord('e')], '1')
        self.assertEqual(huff_codes[ord('b')], '00')
        self.assertEqual(huff_codes[ord('d')], '01')

        #Test with infile3.txt (huffman example)
        freq_list3 = cnt_freq("in_file_3.txt")
        huff_tree_root3 = create_huff_tree(freq_list3)
        huff_codes3 = create_code(huff_tree_root3)
        self.assertEqual(huff_codes3[ord(' ')], '00')
        self.assertEqual(huff_codes3[ord('b')], '01')
        self.assertEqual(huff_codes3[ord('d')], '100')
        self.assertEqual(huff_codes3[ord('c')], '101')
        self.assertEqual(huff_codes3[ord('a')], '11')



    def test_create_header(self):
        #test with infile.txt
        freq_list = cnt_freq("in_file.txt")
        self.assertEqual(create_header(freq_list), "98 1 100 1 101 2\n")

        #test with infile3.txt (huffman example)
        freqList3 = cnt_freq("in_file_3.txt")
        self.assertEqual(create_header(freqList3), "32 3 97 4 98 3 99 2 100 1\n")

        #edge case #1 (one char)
        freqList4 = cnt_freq("edgecase1.txt")
        self.assertEqual(create_header(freqList4), "97 5\n")

    def test_huffman_encode(self):
        #test with infile.txt
        huffman_encode("in_file.txt", "out_file.txt")
        self.assertTrue("out_file.txt", "out_file_sol.txt")

        # test with infile3.txt (huffman example)
        huffman_encode("in_file_3.txt", "out_file.txt")
        self.assertTrue("out_file.txt", "out_file_sol2.txt")

        #test with edcase#2 (empty infile)
        huffman_encode("edgecase#2.txt", "out_file.txt")
        self.assertTrue("out_file.txt", "edgecase#2_sol.txt")

        #test edgecase#3 (no file)
        with self.assertRaises(FileNotFoundError):
            huffman_encode("deez.txt", "out_file.txt")


if __name__ == "__main__":
    unittest.main()
