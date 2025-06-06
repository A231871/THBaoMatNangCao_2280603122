def checkprime(n):
    #Check if a number is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if checkprime(number):
    print("The number " + str(number) + " is prime.")
else:
    print("The number " + str(number) + " is not prime.")
# The code above checks if a number is prime by checking if it is divisible by any number from 2 to the square root of the number.