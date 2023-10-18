first_number = int(input("Enter Number: "))
second_number = int(input("Enter Number: "))
if first_number > second_number:
    largest_number = first_number
else:
    largest_number = second_number
gcd = largest_number
for i in range(1, largest_number + 1):
    if (first_number % i == 0) and (second_number % i == 0):
        gcd = i 
print(gcd)