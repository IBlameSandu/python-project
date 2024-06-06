import random, math
from kiez_kand import Kiezer, Kandidaat, Lijst
from stemsysteem import Stembus, Scanner, Stemcomputer, Chipkaart, USBStick
from toHTML import parser

def main():
    #Een paar dictionaries aanmaken.
    lijsten={}
    Kiezers={}

    #partijen aanmaken.
    for x in range(5):
        lijsten[f"Partij{x+1}"]=Lijst(f"Partij{x+1}")

    print("partijen werden aangemaakt.")

    #Kiezers en kandidaten aanmaken, de kandidaten worden ook direct in hun partij gezet.
    count=1
    for x in range(1200):
        if x < 50:
            if lijsten[f"Partij{count}"].aantalKandidaten() >= lijsten[f"Partij{count}"].maxKandidaten:
                count += 1
            kandidaat=Kandidaat(x)
            lijsten[f"Partij{count}"].addKandidaat(kandidaat)
            Kiezers[f"kiezer{x}"]=kandidaat
        else:
            Kiezers[f"kiezer{x}"]=Kiezer(x)
    print("kiezers en kandidaten werden aangemaakt.")
    
    #print(f"werkt volledig, kiezer lengte {len(Kiezers)}, 50 kandidaten")

    usb=USBStick()
    scann=Scanner()
    stembus=Stembus()
    stembus.geefCodeUSB(usb)
    stemcomputer1=Stemcomputer(usb)
    stemcomputer2=Stemcomputer(usb)
    stemcomputer3=Stemcomputer(usb)
    print("stemcomputers, usb, stembus en scanner aangemaakt!")
    #nummer=0
    with open("output.txt", "w") as output:
        for kiezer in Kiezers.values():
            chipkaarten={}
            for x in range(60):
                chipkaarten[f"chipkaart{x}"] = Chipkaart()
            randomNummer=math.floor(random.random()*60)
            chipkaartVanDeKiezer=chipkaarten[f"chipkaart{randomNummer}"]

            output.write(f"60 chipkaarten werden geïnitialiseerd\n")
            output.write(f"kiezer {kiezer.getName()} kreeg chipkaart {randomNummer} met opstartcode {chipkaartVanDeKiezer.getOpstart()}\n")

            #nummer+=60
            stemcomputer1.stemmen(kiezer, chipkaartVanDeKiezer, lijsten)
            stemcomputer2.stemmen(kiezer, chipkaartVanDeKiezer, lijsten)
            stemcomputer3.stemmen(kiezer, chipkaartVanDeKiezer, lijsten)

            output.write(f"kiezer {kiezer.getName()} heeft zijn stem ingevoerd\n")

            if kiezer.heeftGestemd():
                stem=stemcomputer3.geefStembil(kiezer)
                output.write(f"kiezer {kiezer.getName()} zijn stem wordt gevalideerd!\n")

                scann.check(stem)
                stembus.addStembil(stem)
                output.write(f"{kiezer.getName()} heeft succesvol gestemd!\n\n")

    output.close() #voor de zekerheid

    parser(lijsten)
    print("Een tekst bestand met de volledige output is nu beschikbaar!")
    print("De HTML output van de verkiezingen is nu beschikbaar!")
    #for lijst in lijsten.values():
        #for x in lijst.getKandidaten():
            #print(f"kandidaat {x.getName()} heeft {x.getStemmen()} stemmen")
    #print(f"er werden {nummer/1200} chipkaarten aangemaakt voor elk kiezer")

if __name__=="__main__":
    main()