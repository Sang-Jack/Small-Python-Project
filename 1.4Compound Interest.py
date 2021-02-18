#function which takes one parameter (amount deposited by the user)
#And the function return the interset he gain
def interest(amount):
    amount=amount+(amount*0.04)
    return amount

#Asking the user how much amount he wants to deposit in his savings account
#i would like to take the amount as float
amount=float(input("Enter the amount of money you want to deposit:"))

#calling the interest function and that function computes the interest
#and that interest is added to the amount
amount=interest(amount)

#The balance of the savings account after 1 year
#while printing the amount we rounded the amount to 2 decimals using round()function
print("The amount in your savings account after 1 year is:",round(amount,2))
amount=interest(amount)

#The balance of the savings account after 2 years
print("The amount in your savings account after 2 years is:",round(amount,2))
amount=interest(amount)

#The balance of the savings account after 3 years
print("The amount in your savings account after 3 years is:",round(amount,2))
