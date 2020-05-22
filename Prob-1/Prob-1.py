# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Matthew Bly

# Input: a number between one a ten
# Process: converts integer to a roman numeral
# Output: Roman numeral value of the inputted integar

# function definition
def romanNumeral(number):
    if number  == 1:
        return "I"
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    elif number == 6:
        return 'VI'
    elif number == 7:
        return 'VII'
    elif number == 8:
        return 'VIII'
    elif number == 9:
        return 'IX'
    elif number == 10:
        return 'X'
    else:
        return 'unknown'

# unit test function
def unitTest():
    print()
    print('Number: 1\tRoman Numeral:', romanNumeral(1))
    print('Number: 2\tRoman Numeral:', romanNumeral(2))
    print('Number: 3\tRoman Numeral:', romanNumeral(3))
    print('Number: 4\tRoman Numeral:', romanNumeral(4))
    print('Number: 5\tRoman Numeral:', romanNumeral(5))
    print('Number: 6\tRoman Numeral:', romanNumeral(6))
    print('Number: 7\tRoman Numeral:', romanNumeral(7))
    print('Number: 8\tRoman Numeral:', romanNumeral(8))
    print('Number: 9\tRoman Numeral:', romanNumeral(9))
    print('Number: 10\tRoman Numeral:', romanNumeral(10))
    print()

def main():
    romanNumeral

unitTest()
main()