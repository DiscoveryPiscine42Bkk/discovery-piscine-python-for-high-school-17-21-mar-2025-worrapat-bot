#!/usr/bin/env python3
number_a = int(input(""))
number_b = int(input(""))

result = number_a * number_b

print(result)

if result < 0:
    print("The result is negative.")

elif result > 0:
    print("The result is positive.")

else:
    print("The result is positive and negative.")

