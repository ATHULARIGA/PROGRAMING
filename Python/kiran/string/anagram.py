def are_anagrams(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    if len(str_num1) != len(str_num2):
        return False
    sorted_num1 = sorted(str_num1)
    sorted_num2 = sorted(str_num2)

    return sorted_num1 == sorted_num2

# Example usage:
num1 = 12345
num2 = 54321

if are_anagrams(num1, num2):
    print(f"{num1} and {num2} are anagrams.")
else:
    print(f"{num1} and {num2} are not anagrams.")