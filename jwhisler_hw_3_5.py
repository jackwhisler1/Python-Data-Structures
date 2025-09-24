"""
Jon Whisler

Class: CS 521 - Fall 

Date: 9/18/2025

Homework Problem # 3_5

Description: Determines how many rooms have matching birthdates using random integers. 
"""
import random
TESTS = 50
SIZE = 30

rooms = []
for i in range(TESTS):
  temp_room = []
  for i in range(SIZE):
    temp_room.append(random.randint(1,365))
  rooms.append(temp_room)

birthday_rooms = [room for room in rooms if len(room) != len(set(room))]
total_birthday_rooms = len(birthday_rooms)

print(
  f"Of {TESTS} rooms of {SIZE} people each, there were {total_birthday_rooms} "
  "matching birthdates. \n"
  f"This is a matching percentage of {round((total_birthday_rooms / TESTS * 100), 2)}%"
)