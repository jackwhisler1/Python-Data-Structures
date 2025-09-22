#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Return number of menu items and numbered list of each item.


@author: jnwhisler
"""
menu = ["ham", "eggs", "bacon", "fish", "toast", "spam", "congee", "fruit"]
print("Welcome to best breakfast buffet! " 
      f"We have {len(menu)} items available.")
for i in range(0, len(menu)):
    print(f"{i + 1}. {menu[i]}")
