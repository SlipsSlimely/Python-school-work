#Paul Bahdouchi
#This program will find MPH using a formula involving KPH

print ("KPH\tMPH")
print ("____________")

Start_speed = 60 #this is the start speed in KPH
End_speed = 131 #this is the end speed in KPH
increment = 10 #this is the number that KPH increases by
Multiplier = 0.6214 #this is the number that multipies with KPh to solve for MPH
#this equation takes KPH and solves for MPH (MPH = KPH * 0.6214) 

for KPH in range (Start_speed, End_speed, increment):
    MPH = KPH * Multiplier
    print (KPH,"\t", format(MPH, '.0f') )
#this is a for loop

print ("KPH\tMPH")
print ("____________")
KPH = Start_speed
while KPH < End_speed:
    MPH = KPH * Multiplier
    print (KPH, "\t", int(MPH))
    KPH = KPH + increment
#this is the while loop

