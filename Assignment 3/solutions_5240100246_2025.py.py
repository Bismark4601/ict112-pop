"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "Programming"
reversed_string(original_string)
print(f"original_string: {original_string}")
print(f"reversed string: {reversed_string}")

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
""" 
full_name = input("Enter your full_name:")
initials = get_initials(full_name)
print(f"initials: {initials}")


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string = input("Enter string:")
print(is_palindrome(string))
def is_palindrome(string):
    if(string) == string[::-1]:
     return"The string is palindrome."
    else:
        return"The string is not a palindrome."



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
test_string = "Kofi is a boy"
print("The original string is: " + test_string)
res = len(test_string.split())
print("The number of words in string is: " + str(res))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example"
modified_string = replace_is_word(original_string)
print(f"original_string: {original_string}")
print(f"modified_string: {modified_string}")
