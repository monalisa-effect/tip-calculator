#If the bill was $150.00, split between 5 people, with 12% tip. 
print('Welcome to the tip calculator!')
print('What was the total bill? ')
bill = float(input())
tip_per = print('How much tip would you like to give? 10, 12, or 15?')

tip_per = float(input())


tip_per = float(tip_per) /100  

print(type(bill))




#Each person should pay (150.00 / 5) * 1.12 = 33.6
print("How many people to split the bill?")
ppl = float(input())

result = (bill + (bill * tip_per)) / ppl

result = round(result, 2)

print(result)

#Format the result to 2 decimal places = 33.60


#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


#Write your code below this line 👇