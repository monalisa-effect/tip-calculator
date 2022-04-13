#If the bill was $150.00, split between 5 people, with 12% tip. 
print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? '))
tip_per = float(input('How much tip would you like to give? 10, 12, or 15?'))

tip_per = float(tip_per) /100  

#Each person should pay (150.00 / 5) * 1.12 = 33.6

ppl = float(input("How many people to split the bill?"))

result = (bill + (bill * tip_per)) / ppl


#Format the result to 2 decimal places = 33.60


#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
result = round(result, 2)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")


#Write your code below this line 👇
