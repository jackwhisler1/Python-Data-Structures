"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_5

Description: 
"""
MENU_ITEMS = {"ham": 4.40, "eggs": 2.85, "bacon": 1.00,
              "fish": 12.50, "toast": .90, "spam": .50, "fruit": .85}

print("Welcome to the Breakfast Café!")
print("Here is out menu for today:")
i = 1

for k, v in MENU_ITEMS.items():
    print(f"{i}. {k:<10}      ${v:>5.2f}")
    i += 1
