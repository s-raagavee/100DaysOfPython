#Task: Get user inputs for the bill, tip percentage and how many people
# to split it with and calucate how much each person owes.

#print welcome Message
print("Welcome to the tip calculator!")

#get total bill from user
bill = float(input("What was the total bill? $"))

#get percentage of tip user want to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#get how many people to spilt bill with from user
ppl = int(input("How many people to split the bill? "))

#calulate total bill
total_bill = (bill * (1 + (tip/100))) / ppl

#print how much each person owes to 2 d.p
print(f"Each person should pay: ${total_bill:.2f}")