num = int(input("Enter any number: "))
n = num%2
if n == 0:
    print(num, "is an even number")
elif n == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")