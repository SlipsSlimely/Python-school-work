# Paul Bahdouchi
# Star pyramid code 
size = 1469
character= "*"
for row in range ( size) :
    for column in range (size,row, -1) :
        print (character,end=' ')
    print ( )
