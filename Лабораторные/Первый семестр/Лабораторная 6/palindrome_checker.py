from stack import Stack

def is_palindrome(string):
    stack = Stack(len(string))
    
    for char in string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return string == reversed_string

if __name__ == "__main__":
    test_string = input("Введите строку для проверки на палиндром: ").strip()
    if is_palindrome(test_string):
        print(f"'{test_string}' является палиндромом!")
    else:
        print(f"'{test_string}' не является палиндромом.")
