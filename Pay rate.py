hours_worked = float (input ("What are the hours you worked: "))

pay_rate = float (input ("What is your pay rate: ")) #outputs a input box 

gross_pay = hours_worked * pay_rate #calculates gross pay

print ("My gross pay for ",format(hours_worked,'.2f'),"hours worked at"\
       ,format(pay_rate,'.2f'),"per hour"\
       " is: $", format(gross_pay,',.2f'))


