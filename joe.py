#Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:

#The number of shares that Joe purchased was 2,000.
#When Joe purchased the stock, he paid $40.00 per share.
#Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.
#Two weeks later Joe sold the stock. Here are the details of the sale:

#The number of shares that Joe sold was 2,000.
#He sold the stock for $42.75 per share.
#He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
#Write a program that displays the following information:

#The amount of money Joe paid for the stock.
#The amount of commission Joe paid his broker when he bought the stock.
#The amount that Joe sold the stock for.
#The amount of commission Joe paid his broker when he sold the stock.
#Display the amount of money that Joe had left when he sold the stock and paid his broker (both times).
#If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

#below is code to work with

#hours_worked = float (input ("What are the hours you worked: "))

#pay_rate = float (input ("What is your pay rate: ")) 

#gross_pay = hours_worked * pay_rate 

#print ("My gross pay for ",format(hours_worked,'.2f'),"hours worked at"\
       #,format(pay_rate,'.2f'),"per hour"\
       #" is: $", format(gross_pay,',.2f'))

#above is code to work with

shares = float (2000)
Oshare_price =  float ("40.00") #this is the price he bought the shares at
Eshare_price =  float ("42.75") #this is the price he sold the shares for
commission = float ("0.03") #this is the percent on commission joe paid

Ostockbroker_pay = commission * ( Oshare_price * shares ) #this equation shows how much the broker got at the original price

Estockbroker_pay = commission * ( Eshare_price * shares ) #this equation shows how much the broker got at the sale price

paid = shares * Oshare_price #this shows how much joe paid

made = Eshare_price * shares #this shows how much joe made before taking away original cost

paid_originally = Ostockbroker_pay + paid #this shows how much joe paid when he bought the stock and paid the broker

true_made = made - ( paid_originally + Estockbroker_pay ) #this is how much joe actually made

print ("Joe made ", true_made ,"after paying his broker and accounting for what he paid originally")

print ("Joe paid ", paid ,"dollars for his stock before paying his broker")

print ("Joe paid ", Ostockbroker_pay ,"dollars to his Broker initially")

print ("Joe paid ", Estockbroker_pay ,"dollars to his Broker when he sold his stock")

print ("Joe sold the stock and made ", made ,"this is before accounting for what he paid for the stocks" )




