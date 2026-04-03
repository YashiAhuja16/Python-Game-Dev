studentdetails = ("Yashi",89) 

# packing
address = ('227','Meadow Drive','San Ramon','California')
for i in address:
    print(i,end =' ')

# unpacking 
house_number, street_name, city, state = address 
print(house_number)
print(street_name)
print(city)
print(state) 

mytupple = 328, 283, 36.9, 1625, 972, 463, 'Glass'
print(mytupple)

# nested tupple
endtupple = (293, 746.9, 192, 376, 'Bowl', ('Desk', 372, 195, 478))  
print(endtupple[5][3])

# tupple slicing
mytupple = ('P','R','O','G','R','A','M','M','I','N','G')
print(mytupple[:-7])

# changing tupple values
# mytupple[2] = "A" 
personaltupple = (183.8, 291, "Picture", 384, [182, 2932])
personaltupple[4][1] = 283 
print(personaltupple)
yourtupple = ('P','R','O','G','R','A','M','M','I','N','G')
print(yourtupple) 