from stack_array import Stack

'''Creating a dictionary that stores the operators and the order of importance'''
ops = {"(": 1, "-": 2, "+": 2, "*": 3, "/": 3, "**": 4, "<<": 5, ">>": 5}

'''Create PostfixFormatException class to call error messages:'''


class PostfixFormatException(Exception):
    pass


'''helper function to check if string input is a number (int, float, positive or negative)'''


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def postfix_eval(postfix_expr):
    if postfix_expr.strip() == "":
        raise PostfixFormatException("Empty input")
    num_Stack = Stack()
    num_List = postfix_expr.split()
    for value in num_List:
        # Check if value passed is an operator
        if value in ops:
            # There must be 2 numbers in order for an operator to be executed
            if num_Stack.size() < 2:
                raise PostfixFormatException("Insufficient Operands")
            num2 = num_Stack.pop()
            num1 = num_Stack.pop()
            if value == "+":
                result = num1 + num2
            elif value == "-":
                result = num1 - num2
            elif value == "/":
                if num2 == 0:
                    raise ValueError
                result = round((num1 / num2), 2)
            elif value == "*":
                result = num1 * num2
            elif value == "**":
                result = num1 ** num2
            elif value == "<<":
                try:
                    result = num1 << num2
                except TypeError:
                    raise PostfixFormatException("Illegal bit shift operand")
            elif value == ">>":
                try:
                    result = num1 >> num2
                except TypeError:
                    raise PostfixFormatException("Illegal bit shift operand")

            # Push result to num_stack after each operation is performed
            num_Stack.push(result)
        elif isInt(value) == True:
            num_Stack.push(int(value))
        elif isFloat(value) == True:
            num_Stack.push(float(value))
        else:
            raise PostfixFormatException("Invalid token")
    # After operators are executed there should only be one item in num_Stack (the result)
    if num_Stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return num_Stack.pop()


def infix_to_postfix(infix_str):
    op_Stack = Stack()
    RPN_expr = []
    infix_List = infix_str.split()
    for value in infix_List:
        if isFloat(value) == True:
            RPN_expr.append(value)
        elif value == "(":
            op_Stack.push(value)
        elif value == ")":
            while op_Stack.peek() != "(":
                RPN_expr.append(op_Stack.pop())
            op_Stack.pop()
        elif value in ops:
            op1 = value
            # In the beginning there won't be an operator inside the stack so we must push op1 first
            if op_Stack.is_empty():
                op_Stack.push(op1)
                continue
            else:
                op2 = op_Stack.peek()
                while (op_Stack.is_empty() == False) and ((op1 != "**" and ops[op1] <= ops[op2])
                                                          or (op1 == "**" and ops[op1] < ops[op2])):
                    temp = op_Stack.pop()
                    RPN_expr.append(temp)
                    if op_Stack.is_empty() == True:
                        break
                    else:
                        op2 = op_Stack.peek()
                op_Stack.push(op1)
    while op_Stack.is_empty() == False:
        remaining_ops = op_Stack.pop()
        RPN_expr.append(remaining_ops)

    # Return RPN expression as a string
    return " ".join(RPN_expr)


def prefix_to_postfix(prefix_str: str):
    # Create a list with each element being separated
    prefix_List = prefix_str.split()
    reverse_prefix = []
    for value in prefix_List[::-1]:
        reverse_prefix.append(value)
    operand_Stack = Stack()
    for element in reverse_prefix:
        if element in ops:
            op1 = operand_Stack.pop()
            op2 = operand_Stack.pop()
            postfix_expr = op1 + " " + op2 + " " + element
            operand_Stack.push(postfix_expr)
        else:
            operand_Stack.push(element)
    # There will only be one item remaining which is the finished postfix expression
    return operand_Stack.peek()
