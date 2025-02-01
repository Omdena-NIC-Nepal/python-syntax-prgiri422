import pytest
from assignment import *

def test_format_string():
    assert format_string("John", 25) == "My name is John and I am 25 years old"
    assert format_string("Alice", 30) == "My name is Alice and I am 30 years old"
    assert format_string("Prabin", 30) == "My name is Prabin and I am 30 years old"

def test_conditional_check():
    assert conditional_check(15) == "Greater"
    assert conditional_check(5) == "Lesser"
    assert conditional_check(10) == "Equal"
    assert conditional_check(-10) == "Lesser"

def test_loop_sum():
    assert loop_sum(5) == 15
    assert loop_sum(3) == 6
    assert loop_sum(1) == 1
    assert loop_sum(100) == 5050

def test_list_operations():
    assert list_operations([1, 2, 3, 4, 5]) == (15, 5, 1)
    assert list_operations([10, 20, 30]) == (60, 30, 10)
    assert list_operations([0,5,10,-5,15]) == (25,15,-5)

def test_dict_operations():
    students = {
        "John": 85,
        "Alice": 90,
        "Bob": 75,
        "Eve": 95
    }
    result = dict_operations(students)
    assert set(result) == {"John", "Alice", "Eve"}
    students = {
        "Prabin": 85,
        "Elon": 90,
        "Evan": 80,
        "Eve": 100
    }
    result = dict_operations(students)
    assert set(result) == {"Prabin", "Elon", "Eve"}

def test_set_operations():
    assert set_operations([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert set_operations([1, 2], [3, 4]) == set()
    assert set_operations([1, 5,10], [10, 15]) == {10}

def test_arithmetic_ops():
    result = arithmetic_ops(10, 5)
    assert result["sum"] == 15
    assert result["difference"] == 5
    assert result["product"] == 50
    assert result["quotient"] == 2.0
    result = arithmetic_ops(5, 0)
    assert result["sum"] == 5
    assert result["difference"] == 5
    assert result["product"] == 0
    assert result["quotient"] == "can't divide by 0"

def test_logical_ops():
    result = logical_ops(True, False)
    assert result["and"] == False
    assert result["or"] == True
    assert result["not_x"] == False
    result = logical_ops(True, True)
    assert result["and"] == True
    assert result["or"] == True
    assert result["not_x"] == False
    result = logical_ops(False, False)
    assert result["and"] == False
    assert result["or"] == False
    assert result["not_x"] == True
def test_bitwise_ops():
    result = bitwise_ops(12, 10)
    assert result["and"] == 8
    assert result["or"] == 14
    assert result["xor"] == 6
    result = bitwise_ops(3, 9)
    assert result["and"] == 1
    assert result["or"] == 11
    assert result["xor"] == 10