#The end user will input the hours worked and their pay rate.
#If the hours worked are over 40,
#then computer needs to calculate the number of hours of overtime.
#Overtime pay rate is 1.5 times normal pay rate.
#If there is no overtime, calculate gross pay normally.
#Display a message on the screen that tells the user the gross
#pay they would receive.
#Format your output for two (2) decimal places and include comma (,) as a
#separator for the value. 

#base hours = 40

#overtime pay rate = 1.5



#overtime hours = hours worked - base hours

#overtime pay = over time hours * pay rate * over time pay rate

#gross pay with overtime = (base hours * pay rate) + overtime pay



#gross pay without overtime = hours worked * pay rate


#Student name: Paul Bahdouchi
#assignment: week three pay rate
#Bhours = base hours = 40
#hours_worked = an input that takes hours worked from a person
#Ohours = overtime hours
#pay_rate = 8.50 dollars per hour
#Opay_rate = 12.75 dollars per hour
#overtime_pay = overtime money made
#gross_pay = money made if hours are under 40
#Ogross_pay = money made if hours are over 40


Bhours = 40 #this is the base hours before overtime

hours_worked = float (input ("What are the hours you worked: ") ) #this asks for
                                                                   #hours worked
Ohours = hours_worked - Bhours #this calculates overtime hours

Thours = hours_worked #this is just an easier thing for hours worked

pay_rate =  float ("8.50") #base pay in the U.S.

Opay_rate = float ("12.75") #this calculates the overtime pay rate

overtime_pay = Ohours * Opay_rate #this calculates overtime pay

gross_pay = Thours * pay_rate #this calculates gross pay before 40 hours

Ogross_pay = gross_pay + overtime_pay #this calculates overtime pay + gross pay

 


if (hours_worked <= 40):
    print ( "this is your gross pay ", format(gross_pay,',.2f'))
else:
    print ( "This is your gross pay including overtime ", format(Ogross_pay,',.2f'))
      
