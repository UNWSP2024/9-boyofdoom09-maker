# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
Range = int(input('How many random numbers would you like in your file? ',))

if Range < 1000:
    for i in range(Range):
        bob = random.randint(1,500)
        print(bob)
else: 
    print('The number must be less than 1,000')
# come back to this one and Don't forget to put the stuff in a file (thumbs up)
