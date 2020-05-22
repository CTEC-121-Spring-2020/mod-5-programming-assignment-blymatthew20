# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Matthew Bly

# Input: Cost of the item and amound tendered
# Process: The amount of change due
# Output: The amount of change given in tens, fives, ones, quarters, dimes, nickles, and pennies

# function definition
def changeCalculator(totalCost, amountTendered):
    changeDue = amountTendered - totalCost
    print(changeDue)

    # converts to an int
    changeDue = int(round(changeDue *100))
    print("change due:", changeDue)

    # calcuate number of tens
    tens = changeDue // 1000
    if tens >= 1:
        print("tens:", tens)
    # adjust changedue to reflect change given
    changeDue = changeDue -(tens * 1000)
    
    # calculate number of fives
    fives = changeDue // 500
    if fives >= 1:
        print('fives:',fives)
    #adjust change due
    changeDue = changeDue - (fives * 500)
    
    # calculate number of ones
    ones = changeDue // 100
    if ones >= 1:
        print('ones:', ones)
    changeDue = changeDue - (ones * 100)
    
    # calculate number of quarters
    quarters = changeDue // 25
    if quarters >= 1:
        print('quarters:',quarters)
    changeDue = changeDue - (quarters * 25)
    
    # calculate number of dimes
    dimes = changeDue // 10
    if dimes >= 1:
        print('dimes:',dimes)
    changeDue = changeDue - (dimes * 10)

    # calculate number of nickles
    nickles = changeDue // 5
    if nickles >= 1:
        print('nickles:',nickles)
    changeDue = changeDue - (dimes * 5)
    
    # calculate number of pennies
    pennies = changeDue // 1
    if pennies >= 1:
        print('pennies:',pennies)
    changeDue = changeDue - (pennies * 1)
    
# main function definition
def main():
    print()
    ItemCost = float(input("Enter the cost of the item:"))
    print(ItemCost)
    amountTendered = float(input('Enter the amount tendered:'))
    print()
    changeCalculator(ItemCost, amountTendered)

main()