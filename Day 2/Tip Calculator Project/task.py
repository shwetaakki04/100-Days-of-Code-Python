print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people =int(input("how many people to split the bill?"))
final_bill = ((bill*(tip/100))+bill)/people
total_bill = print("each person should pay:",final_bill)



