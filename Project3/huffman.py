from ordered_list import *
from huffman_bit_writer import *


class HuffmanNode:
    '''Node for use with doubly-linked list'''

    def __init__(self, character):
        # self.char_in_ascii = ord(character)
        self.char = character
        self.count = 0
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count == other.count:
            if ord(self.char) < ord(other.char):
                return True
        return False


def cnt_freq(filename):
    try:
        #open filename and store in string
        f = open(filename, "r")
        file_contents = f.read()
        # create list that stores frequencies of each char found in filename
        char_counts = [0] * 256
        for char in file_contents:
            #increment frequency count in each index that matches a character from file
            char_counts[ord(char)] += 1
        f.close()
        return char_counts
    except:
        raise FileNotFoundError("File doesn't exist!")


# class HuffmanTree:


def create_huff_tree(list_of_freqs):
    huff_list = OrderedList()
    root_node = None
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] >= 1:
            new_node = HuffmanNode(chr(i))
            new_node.count = list_of_freqs[i]
            huff_list.add(new_node)
    while huff_list.size() > 1:
        # new parentnode char is decided by char with lowest ascii value
        left_child = huff_list.pop(0)
        right_child = huff_list.pop(0)
        if ord(left_child.char) < ord(right_child.char):
            new_parent_char = left_child.char
        else:
            new_parent_char = right_child.char
        new_parent = HuffmanNode(new_parent_char)
        new_parent.count = left_child.count + right_child.count
        new_parent.left = left_child
        new_parent.right = right_child
        huff_list.add(new_parent)
    if huff_list.size() == 1:
        root_node = huff_list.head.next.item
    return root_node


def create_code(root_node: HuffmanNode):
    if root_node is None:
        return
    huffman_code_list = [""] * 256
    huffman_code = ""
    create_code_helper(root_node, huffman_code, huffman_code_list)
    return huffman_code_list


def create_code_helper(leafnode, huffman_code, huffman_code_list):
    # base case to check if we've reached a leafnode
    if leafnode.left is None and leafnode.right is None:
        huffman_code_list[ord(leafnode.char)] = huffman_code
    else:
        # lead node has not been reach so traverse the left and right subtrees recursively
        create_code_helper(leafnode.left, huffman_code + "0", huffman_code_list)
        create_code_helper(leafnode.right, huffman_code + "1", huffman_code_list)
    return True


def create_header(list_of_freqs):
    header = ''
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] >= 1:
            header = header + str(i) + " " + str(list_of_freqs[i]) + " "
    header = header[:len(header) - 1] + "\n"
    return header


def huffman_encode(in_file, out_file):
    freq_list = cnt_freq(in_file)
    huff_tree = create_huff_tree(freq_list)
    file_header = create_header(freq_list)
    huffman_codes = create_code(huff_tree)
    with open(in_file, "r") as file_in:
        file_contents = file_in.read()

    #out_file.txt is first written out with the huffman codes as strings of 0's and 1's (this is done first for debugging purposes and visualization)
    with open(out_file, "w") as file_out:
        #Create header of outfile
        file_out.write(file_header)
        #add the huffmancode sequence that translates the in_file.txt text
        for char in file_contents:
            char_code = huffman_codes[ord(char)]
            file_out.write(char_code)
        file_out.close()

    #adding _compressed before txt to create a compressed file
    out_file = out_file[:len(out_file) - 4] + "_compressed.txt"
    compressed_file = HuffmanBitWriter(out_file)
    #adding header and huffmancode sequence that translates the in_file.txt text
    if huffman_codes is None:
        compressed_file.write_code("")
        compressed_file.close()
    else:
        compressed_file.write_str(file_header)
        compressed_file.write_code(huffman_codes)
        compressed_file.close()

    #out_file.txt is first written with the huffman codes of the input file as string, then it is compressed and written with bits
    # both files are rewritten every time a new input file is added


#print(create_header(cnt_freq("in_file.txt")))
#huffman_encode("in_file_3.txt", "out_file.txt")
#freq_list3 = cnt_freq("in_file_3.txt")
# huff_tree_root3 = create_huff_tree(freq_list3)
