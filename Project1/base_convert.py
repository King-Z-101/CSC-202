def convert(num, b):
    remainder = num % b
    if num < b:
        base_string = str(remainder)
        return base_string
    else:
        if remainder == 10:
            letter = "A"
        elif remainder == 11:
            letter = "B"
        elif remainder == 12:
            letter = "C"
        elif remainder == 13:
            letter = "D"
        elif remainder == 14:
            letter = "E"
        elif remainder == 15:
            letter = "F"
        else:
            letter = str(remainder)
        return convert(num // b, b) + letter


print(convert(30, 5))


# def main():
#     user_input = input()
#     base = input()
#     print(convert(user_input, base))
#
# if __name__ == "__main__":
#     main()

