import random, math
from kiez_kand import Kiezer, Lijst
from stemsysteem import Stembiljet, Stembus, Scanner, Stemcomputer, Chipkaart, USBStick

def main():
    #Een paar dictionaries aanmaken.
    lijsten={}
    Kiezers={}

    #partijen aanmaken.
    for x in range(5):
        lijsten[f"Partij{x+1}"]=Lijst(f"Partij{x+1}")

    #Kiezers en kandidaten aanmaken, de kandidaten worden ook direct in hun partij gezet.
    count=1
    for x in range(1200):
        if x < 50:
            if lijsten[f"Partij{count}"].aantal_kandidaten() >= lijsten[f"Partij{count}"].maxKandidaten:
                count += 1
            lijsten[f"Partij{count}"].add_Kandidaat(Kiezer(x))
            Kiezers[f"kiezer{x}"]=Kiezer(x)
        else:
            Kiezers[f"kiezer{x}"]=Kiezer(x)
    
    
    
    #for x in range(5):
        #print(f"Partij {x+1} heeft {lijsten[f'Partij{x+1}'].aantal_kandidaten()} kandidaten, de kandidaten zijn {lijsten[f'Partij{x+1}']}.")
    #print(Kiezers)
    #print(len(Kiezers))

if __name__=="__main__":
    main()