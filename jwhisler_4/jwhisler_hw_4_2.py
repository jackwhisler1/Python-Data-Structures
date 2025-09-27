"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_2

Description: Simulates a slide-show as a linked list
"""
import random

images = []
for i in range(30):
    images.append("IMG_" + str(random.randint(1000, 9999)))
images.sort(reverse=True)

slideshow = []

for i, e in enumerate(images):
    next_image = ""
    if i == len(images) - 1:
        next_image = "next: " + images[0]
    else:
        next_image = "next: " + images[i + 1]

    slideshow.append((e, next_image))

[print("Image " + e[0] + " (" + e[1] + ")") for e in slideshow]
