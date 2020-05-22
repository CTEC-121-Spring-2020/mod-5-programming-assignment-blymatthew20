# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Matthew Bly

# input: job size in square feet, cost of paint per gallon
# process: calculate estimate
# output: print estimate

FeetPerGallon = 112
LaborHours = 8
LaborCharge = 35

# function definition

def estimate(squareFeet, paintCost):
    print()

    #calculate gallons of paint needed for the job
    PaintGallonsRequired = round(squareFeet / 112)
    print('Gallons of paint required:', PaintGallonsRequired)

    #calculate hours of labor required
    HoursofLabor = round(PaintGallonsRequired * 8)
    print('Labor Hours Required:', HoursofLabor)

    #calculate cost of paint
    PaintCharges =  round(PaintGallonsRequired * paintCost)
    print('Paint Cost:', PaintCharges)

    # calculate labor charges
    LaborCost = round(HoursofLabor * LaborCharge)
    print('Cost of Labor:', LaborCost)

    #setup Fee
    SetupFee = 99.00
    print('Setup Fee:', SetupFee)

    #calculate total cost of the job
    total = round(LaborCost + PaintCharges + SetupFee)
    print('total cost:',total)

    print()

# main function definition

def main():
    print()
    squareFeet = int(input("Enter square feet of wall space to be painted:"))
    paintCost = float(input("Enter price of gallon of paint: "))
    estimate(squareFeet, paintCost)
    print()
 
main()
