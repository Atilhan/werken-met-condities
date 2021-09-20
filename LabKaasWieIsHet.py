Vraag1 = input('Is de kaas geel ?')
if Vraag1 == "Ja":
    Vraag2 = input('Zitten er gaatjes in ?')
    if Vraag2 == "Ja":
        Vraag3 = input('Is de kaas belachelijk duur?')
        if Vraag3 =="Ja":
            print('Emmenthaler')
        else: 
            print('Leerdammer')
    else: 
        Vraag4 = input('Is de kaas hard als steen?')
        if Vraag4 == "Ja":
            print('Pamnigiano Reggiano')    
        else:
            print('Goudse kaas')
else: 
    Vraag5 = input('Heeft de kaas blauwe schimmels?')
    if Vraag5 == "Ja":
        Vraag6 =input('Heeft de kaas een korst ?')
        if Vraag6 == "Ja":
            print('Bleu de RochBaron')
        else:
            print ('Foume D Ambert')
    else:
        Vraag6 =input('Heeft de kaas een korst ?')
        if Vraag6 == "Ja":
            print ('Camembert') 
        else: 
            print('Mozzarella')