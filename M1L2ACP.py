#Create a program to swap three numbers given by the user.

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping logic (rotating the values)
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
