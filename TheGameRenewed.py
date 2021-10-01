#-----------------------------------------------------------Intro van de game------------------------------------------------------------#

print('Je bedacht je op een dag Chernobyl te bezoeken nadat je een spannende reviews & verhalen op het internet had gelezen')
from time import sleep
sleep(3.5)

print('Je besloot om toch een visite te boeken naar Chernobyl of al de verhalen dat je gelezen hebt echt kloppen')
from time import sleep
sleep(3.5)

print('Eenmaal gearriveerd bij Chernobyl heb je gemerkt dat de omgeving een beetje duister voelt')
from time import sleep
sleep(3.5)

print('De weer is grijs en mistig. Je bent bij de ingang gekomen waar een gevaren bord te zien is.')
from time import sleep
sleep(3.5)

print ('*-----------------------------------------------------------------------------------*')
print ('De regels & hoe je de spel moet spelen.')
print ('Er word je een vraag gesteld en binnen in de vraag kan je een antwoord kiezen tussen haakjes zoals (Ja) of (Nee) Je antwoord moet je invullen zoals het daar staat dus met een hoofdletter Ja / Nee')
print ('In de verhalen heb je een time stamp, dus de volgende tekst kom over een paar seconde. ')
print ('Als je verloren hebt, start de game opnieuw ! ')
print ('*-----------------------------------------------------------------------------------*')
from time import sleep
sleep(7.5)
#-----------------------------------------------------------Intro van de game------------------------------------------------------------#

chernobyl = input('Bij de ingang zie je dat er een deur zit tot de Kerncentrale maar er is ook een Basement waar je naar toe kan gaan. Wat kies je ? De (Kerncentrale ?) of (Basement ?) ')
if chernobyl == "Kerncentrale":
    print('Je bent de Kerncentrale binnen gegaan & je zoekt een tijdje rond wat je kan vinden. Na een tijdje heb je een Medische Kit gevonden maar er zit een gat in en je hebt een Box gevonden waar een gevaren tekene op zit')
    from time import sleep
    sleep(5)

    kerncentrale = input ('Je twijfelt over beide keuze maar je hebt besloten om alleen maar één van de gevonden voorwerpen te kiezen , wat kies je ? (Medic Kit) of ( Skull Box ) ')
    if kerncentrale == "Skull Box":
        print('Je hebt de Skull Box gekozen ondanks dat er een gevaren teken op was. Het gevaren bord stond ervoor dat er een wapen in de kist zit, je hebt een wapen gevonden !')
        from time import sleep
        sleep(3.5)
    
        print('Je hebt een wapen gevonden en de lichten van de kamer flickerde voor aantal seconde.')
        from time import sleep
        sleep(3.5)

        print('Een gevoel rilt in je en je bedenkt je de omgeving door te onderzoeken of je misschien de lichten en de energie van de Kerncentrale kan opstarten of toch maar door kan gaan en de basement in de kerncentral te checken. ')
        from time import sleep
        sleep(3.5)

        SkullBox = input('Wat kies je ? (Basement2) of (Onderzoeken)')
        if SkullBox == "Onderzoeken":
           print ('Je besluit toch te onderzoeken en je hebt een machine gevonden waar de kabels eruit liggen')
           from time import sleep
           sleep(3.5)

           Onderzoeken = input('Wil je de kabels weer terug aan de machine vast maken ? (Ja) of (Nee) ')
           if Onderzoeken == "Ja":
               print('De lichten branden weer aan en de ventilatie draait weer waardoor radiatie in de kern reactoren jou richting worden geblazen ')
               from time import sleep
               sleep(3.5)
               print ('Je begint hevig te hoesten & je huid begint te branden ! Helaas foute keuze ! ')
           else:
               print('Doordat je te lang in de centrale bleef ben je heftig geraakt door radiatie , je begint flauw te vallen. Helaas foute keuze !')

        else: 
            print ('Je bent de basement binnen de centrale gegaan waardoor je nu naar beneden bent gegaan. Eenmaal bij de bodem van de basement zie je een schaduw')
            from time import sleep
            sleep(3.5)
            print ('Het is een gemuteerde man die door de radiatie van de kern reactoren gemuteertis  & begint naar je toe te rennen ! .')
            from time import sleep
            sleep(3.5)
            BigShot = input ('Je hebt je wapen in je hand ! , de mutant rent op je af ! Schiet je op zijn lichaam of op de hoofd ? Kies nu ! (Headshot) of (Bodyshot) ')
            Distance = int(input ('De mutant is 100 meter verder op. Je neemt te tijd om te richten. Wanneer begin je met schieten voordat de mutant te dichtbij is ? ( geef meters aan ) '))
            numbers = [1,2,3,4,5,6,7,8,9]
            if (BigShot == "Headshot" and Distance <= 50 and not Distance in numbers) :
                print ('Je hebt de mutant gekilled ! ')
            else:
                print('De mutant heeft je gebeten & opgegeten ! Probeer opnieuw')
    
    else:
        MedicKit = input ('In de medic kit zit een vitamine D supplement in (Gezonde pil) wil je dit innemen ? (Ja) of (Nee) ')
        if MedicKit == "Ja":
            print ('Door de gat in de Medic Kit is alles overlopen door giftig radiatie , Je keel begint pijn te doen & je valt flauw & je hart begint te stoppen met kloppen. Helaas foute keuze !')
        
        else:
            print ('Terwijl je verder in de medic kit zocht raakte er een vloeistof je vingers aan, het is uranium fuel dat gelekt was in de medic kit & een gat veroorzaakte, je begint flauw te vallen. Helaas foute keuze !')

else:
    basement = input ('Je bent de basement binnen. Er zijn 2 kamers met deuren. Welke kamer kies je ? (Kamer1) of (Kamer2)')
    if basement == "Kamer1":
        print ('Je bent voorzicht de kamer binnen gegaan maar er gloeien rode ogen die je aankijken en de deur achter je slaat dicht. Duisternis overkomt je & je bent nu één van hen. Helaas foute keuze !')

    else:
        print('Je bent kamer 2 voorzichtig binnen gegaan.')
        from time import sleep
        sleep(3.5)
        Cell = input ('Je komt een cell tegen waarin een gevangen in zit wat doe je met hem ? (Loslaten) of (Doorgaan)')
        if Cell == "Loslaten":
            print('De gevangenen is gestoort & heeft je van achteren neergestoken. Helaas foute keuze !')
        
        else:
            Outfit = input('Je bent doorgegaan & heb de gevangenen gelaten in zijn cell, er is een kast met kleding van bewakers . Wil je dit meenemen ? (Ja) of (Nee)')
            Mes = input ('Er zijn aantal messen in de zak, hoeveel messen wil je meenemen ? ')
            if Outfit == "Ja" and Mes >=2 and not Mes != 5:
                print ('Je neemt de outfit mee en de mes')
                Guards = input('Je komt een deur tegen en tegenover de andere kant staan 2 bewakers met een wapen. Wil je je kleding aantrekken ? & langs de bewakers gaan ? (Ja) of (Nee)')
                if Guards == "Nee":
                    print ('De bewakers schreeuwen wat je hier te zoeken hebt & beginnen je te schietenHelaas foute keuze !')
                
                else:
                    print('Je hebt de kleding aan gedaan & bent langs de bewakers gelopen en buiten de kerncentrale uitkomen, je bent vrij !')
            
            else:
                print('Je gaat door zonder de outfit mee te nemen')
                RushHour = input('Je komt een deur tegen en tegenover de andere kant staan 2 bewakers met een wapen. Wil je op ze afrennen of doen alsof je verdwaald bent (Afrennen) of (Verdwaald) ? ')
                if RushHour == "Afrennen":
                    print('Je bent al neergeschoten voordat je je eerste stap zette.')
                else:
                    print('De bewakers schieten je neer omdat dit een afgelegen plaats is & een geheime muteer lab is geworden. Helaas foute keuze !')


#Made by Atilhan & Inspired by the Chernobyl Disaster
                    








