# bounce.py
#
# Exercise 1.5

height = 100 #meters
bounce_count = 10
i = 1

while i <= bounce_count:
    height *= 0.6
    i += 1
    print(round(height, 4))