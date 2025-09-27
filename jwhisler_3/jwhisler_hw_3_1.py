"""
Jon Whisler

Class: CS 521 - Fall 

Date: 9/18/2025

Homework Problem # 3_1

Description: Prompts user for dimensions and calculates required amount of 
wrapping paper. Continues to prompt until user types 'quit'.
"""

print(f"-------------------------------------\n"
      "Welcome to the gift-wrap calculator!\n"
      "-------------------------------------")
PROMPT = "Please enter the box dimensions separated with an x" \
    "(ex: 10x20x15) "
user_dimensions = input(PROMPT)
while user_dimensions != "quit":    
    # Converts input to a sorted list of floats
    dimensions = list(map(float, user_dimensions.split('x')))
    dimensions.sort()
    
    required_wrap = round(
        (3 * dimensions[0] * dimensions[1]) + 
        (2 * dimensions[1] * dimensions[2]) + 
        (2 * dimensions[0] * dimensions[2]), 
        2
    )
                    
    print(f"You will need {required_wrap}cm of wrapping paper.")
    user_dimensions = input(PROMPT)

print("Thank you for using the gift-wrap calculator!")




