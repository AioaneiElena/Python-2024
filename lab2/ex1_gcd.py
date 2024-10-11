import math

numbers = list(map(int, input("Enter numbers: ").split()))
gcd = numbers[0]
for num in numbers[1:]:
    gcd = math.gcd(gcd, num)

print(f"The GCD of the given numbers is: {gcd}")
