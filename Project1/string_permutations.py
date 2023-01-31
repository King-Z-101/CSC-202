# Function called to print out the list of permutations coming from string
def perm_gen_lex(simple_string):
    if


def main():
    # Create an empty list to store the permutations
    lex_list = []
    # Ask user for input and use it in the perm_gen_lex() function
    long_string = input("Give me a string: ")
    for char in long_string:
        new_string = char
        perm_gen_lex(new_string)
        #lex_list.append(perm_string)


if __name__ == '__main__':
    main()
