dressuur = int (input('hoeveel aantal jaren heeft u ervaring in dressuur? '))
jongleren = int (input('hoeveel aantal jaren heeft u ervaring in jongleren? '))
acrobatiek = int (input('hoeveel aantal jaren heeft u ervaring in acrobatiek? '))
mbo = input('heeft u uw MBO4 diploma ondernemen binnen ? ')
rijbewijs =input('heeft u een vrachtwagen rijbewijs ?')
hoed = input('heeft u een hoed in uw bezit? ')
certificaat = input("heeft u een 'Overleven met gevaarlijk personeel' certificaat ? ")
lengte = int(input('wat is uw lengte ? '))
gewicht = int(input('wat is uw gewicht? '))
gender = input('bent u een man of een vrouw?')
#snor = int (input('hoelang is uw snor ? '))
#haar = int(input('hoelang is uw krulhaar ? '))
#lengtehaar = int(input('is uw haar rood ?))


if gender == "man":
    snorlengte = input('heeft u een snor ?')
    if snorlengte =="ja":
        snor = int (input('hoelang is uw snor ? '))
    else:
        print('Pech gehad, je bent niet aangenomen')

else:
    lengtehaar = str(input('is uw haar rood & krullig ?'))

    if lengtehaar =="ja":
        haar = int(input('hoelang is uw krulhaar ? '))
    else:
        print('Pech gehad, je bent niet aangenomen')

if (dressuur >= 4 or jongleren >= 5 or acrobatiek  >= 3) and mbo == "ja" and rijbewijs == "ja" and hoed == "ja" and certificaat == "ja" and gewicht >= 90 and lengte >= 150 and ((gender == "man" and snor >= 10) or (gender == "vrouw" and haar >= 20 and lengtehaar == "ja")) :
    print('Gefeliciteerd, je bent aangenomen ! ')

else:
    print('Pech gehad, je bent niet aangenomen')

