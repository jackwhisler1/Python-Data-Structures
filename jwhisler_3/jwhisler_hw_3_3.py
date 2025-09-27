"""
Jon Whisler

Class: CS 521 - Fall 

Date: 9/18/2025

Homework Problem # 3_3

Description: Allow user to order item off the menu, by number name
"""
MENU = ["ham", "eggs", "bacon", "fish", "toast", "spam", "fruit"]

print("Welcome to the Breakfast Café!")

print("Please select a menu item.")
order = ""
while order.lower() not in MENU:
  for i in range(0, len(MENU)):
      print(f"{i + 1}. {MENU[i]}")

  order = input("Your order? ")
  try:
    order_number = int(order)
    if MENU[order_number - 1]:
      order = MENU[order_number - 1]
  except:
    pass
  if order.lower() not in MENU: 
    print("Sorry, I don't think we carry that.")
  else:
    print(f"One order of {order} coming right up!")
    break
