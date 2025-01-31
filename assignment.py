def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return (f"My name is {name} and I am {age} years old")
    

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10 :
        return ("Greater")
    elif number < 10 :
        return "Lesser"
    else :
        return "Equal"
  

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    loop_sum = 0
    for i in range(1,n+1) :
        loop_sum += i
    return loop_sum
 

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    Total_sum = sum(numbers)
    Max_value = max(numbers)
    Min_value = min(numbers)
    return Total_sum,Max_value,Min_value


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    return [name for name, scores in students_dict.items() if scores > 80 ]
    
   

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1) & set(list2)
   

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return{
        "sum": a+b,
        "difference": a-b,
        "product": a*b,
        "quotient": a/b if b!=0 else "can't divide by 0"
    }
   

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return{
        "and" : x and y,
        "or" : x or y ,
        "not_x" : not x
        }
   

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return{
        "and" : a & b,
        "or" : a | b,
        "xor" : a ^ b
    }
   