# Name: Paul Bahdouchi

# Loan Qualifier V2.0

# This program takes in the input of a user to find their salary and then tells
# them whether or not they qualify for a loan


Msalary = 30000 #this is the minimum salary required for the loan
print ( "The minimum salary for qualifying: $", format(Msalary,',.0f') ) 
Csalary = float (input ("What is your salary: ") )

if (Csalary >= Msalary) :
    print ( "Your current salary qualifies you for the loan. Congratulations!" )
else:
    print ( "Your current salary does not qualify you for the loan. So sorry!" )
