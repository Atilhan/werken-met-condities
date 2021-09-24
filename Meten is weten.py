#-----------------------------------------------------------#
#                         Grootste Getal Methode            #
a = int (input('Vul een heel getal in '))
b = int (input('Vul een heel getal in '))

if a > b:  
    print (int(a) , str('Is het grootste getal'))

else:
    print (int(b) , str('Is het grootste getal'))

#-----------------------------------------------------------#
#                         Kleinste Getal Methode            #
c = int (input('Vul een heel getal in '))
d = int (input('Vul een heel getal in '))

if c < d:
    print (int(c) , str('Is het kleinste getal'))

else:
    print (int(d) , str('Is het kleinste getal')) 

#-----------------------------------------------------------#
#                         Minimaals & Maximaals             #

a = int (input('Vul een heel getal in '))
b = int (input('Vul een heel getal in '))

if a > b:
    max = a
    min = b

elif a < b:
    max = b
    min = a

print("Het minimum getal is" , min)
print("Het maximum getal is", max)

#-----------------------------------------------------------#

