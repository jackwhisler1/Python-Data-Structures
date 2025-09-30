"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_5

Description: Adds to the cafe concept and allows a user to input orders, calculates total cost upon inputting 'done'.
"""
MENU_ITEMS = {"ham": 4.40, "eggs": 2.85, "bacon": 1.00,
              "fish": 9.50, "toast": .90, "spam": .50, "fruit": .85}

print("Welcome to the Breakfast Café!")
print("Here is out menu for today:")
i = 1

for k, v in MENU_ITEMS.items():
    print(f"   {i}. {k:<10}   ${v:>4.2f}")
    i += 1
order = ''
ordered_items = set()
while order.lower() != 'done':
    order = input(
        "Please enter your selection by name; when finished ordering enter 'done': ")
    order = order.lower().strip()
    if order in MENU_ITEMS:
        ordered_items.add(order)
        print(f"Current Order: {', '.join(ordered_items)}")
    elif order.lower() == 'done':
        if ordered_items:
            print("\nExcellent! Here is your bill:")
            print("----------------------------------------")
            total = 0
            max_item_length = max(len(item) for item in ordered_items)
            for item in ordered_items:
                price = MENU_ITEMS[item]
                print(f"{item.title():<{max_item_length}}   ${price:>5.2f}")
                total += price

            print("----------------------------------------")
            print(f"TOTAL: ${total:>5.2f}")
            print("----------------------------------------")
        else:
            print("You did not order anything.")
    else:
        print("Sorry, I don't think we carry that.")
