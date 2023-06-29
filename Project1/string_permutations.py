# Function called to print out the list of permutations coming from string
def perm_gen_lex(og_string):
    permutation_list = []
    #Return an empty list if no input is found
    if len(og_string) == 0:
        return []
    #Base case used to stop the recursion (found the end of the permutation string)
    if len(og_string) == 1:
        permutation_list = [og_string]
        return permutation_list
    else:
        for char in range(len(og_string)):
            #Remember the removed char so that it can later be appended to each permutation (in the beginning)
            removed_Char = og_string[char]
            #Create simpler string without removed_Char
            simple_string = og_string[:char] + og_string[char + 1:]
            #Finds the different permutations created by the simple_string and appends it to the permutation_list
            for permutation in perm_gen_lex(simple_string):
                permutation_list.append(removed_Char + permutation)
        return permutation_list



# def main():
#     # Create an empty list to store the permutations.
#     lex_list = []
#     # Ask user for input and use it in the perm_gen_lex() function
#     long_string = input("Give me a string: ")
#     for char in long_string:
#         new_string = char
#         perm_gen_lex(new_string)
#         #lex_list.append(perm_string)
#
#
# if __name__ == '__main__':
#     main()
