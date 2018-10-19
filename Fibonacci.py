"""
The Fibonacci Game v1.0
by: Jonathan Chapman
date: September 20, 2018
"""

print("\nWELCOME TO THE FIBONACCI GAME!!!\n")
print("In this game, you enter a number, and I, the computer,\n"\
      "will show you all the numbers in the Fibonacci Sequence\n"\
      "up to that number. Have fun!\n")

while True:
    try:
        userInput = int(input("Enter a number: "))
        break
    except:
        print("Sorry. This is not a number. You must enter a number (without decimals).")
        pass

print("")

fibA = 0
fibB = 1
fibC = fibB
print(fibA)

while fibC <= userInput:
    fibB = fibA + fibC
    fibA = fibC
    fibC = fibB
    print(fibA)