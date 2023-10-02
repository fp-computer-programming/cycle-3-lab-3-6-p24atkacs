"""
Create a Python file named lab_3-6.py

Write a statement that creates the string "Fairfield Prep" by concatenating substrings.

Write a statement that creates a dashed line that is 20 dashes long.

Write a statement that prints the following:
I'm loving this short story I'm reading, "The Fall of the House of Usher"

Write a statement that prints the length of the previous string.

Write a statement using the index operator that returns the "L" in "apple"

"""
prep_string = "Fair" + "field" + " Prep"

dashed_line = "-" * 20

print('I\'m loving this short story I\'m reading, "The Fall of the House of Usher"')

previous_string_length = len('I\'m loving this short story I\'m reading, "The Fall of the House of Usher"')
print("Length of the previous string:", previous_string_length)

apple_string = "apple"
letter_l = apple_string[3]

print("The 4th letter in apple is:", letter_l)
