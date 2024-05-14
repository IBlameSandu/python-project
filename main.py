#nodig om namen willekeurig te kiezen
import random
import math

#namen ophalen v/d bestanden en ze cleanen door de \n weg te halen
vn=[]
voornamen=open("voornamen.txt", 'r')
data=voornamen.readlines()
vn.extend(name.strip('\n') for name in data)
voornamen.close()

an=[]
achternamen=open("achternamen.txt", 'r')
data=achternamen.readlines()
an.extend(name.strip('\n') for name in data)
achternamen.close()

#de partijen (lijsten), maar wel dictionaries gebruikt door creatieve vrijheid en om te testen
#Denver_Nuggets={}
#LA_Lakers={}
#Chicago_Bulls={}
#Miami_Heat={}
#Dallas_Mavericks={}

#klassen aanmaken
class Kiezer:
    def __init__(self, id):
        self.id=id
        self.__voornaam=vn[math.floor(random.random()*len(vn))]
        self.__achternaam=an[math.floor(random.random()*len(an))]
        self.leeftijd=math.floor(random.random()*73)+18
        self.__mogelijkeStemmen=1
    
    def getName(self):
        return f"{self.__voornaam} {self.__achternaam}"
    def __repr__(self):
        return f"{self.__voornaam} {self.__achternaam}, {self.leeftijd}"

class Kandidaat(Kiezer):
    def __init__(self, id):
        super().__init__(id)

class Lijst:
    def __init__(self, naam):
        self.maxKandidaten=10
        self.naam=naam
        self.__kandidaten={}

    def add_Kandidaat(self, kandidaat):
        if len(self.__kandidaten) < self.maxKandidaten:
            self.__kandidaten[kandidaat.getName()]=0

    def __repr__(self):
        return f"{self.__kandidaten}"

class Stembiljet:
    def __init__(self):
        pass

class Stembus:
    def __init__(self, usb):
        self.usb=usb.getOpstart()
        with open("opstartcodes.txt", "r") as bestand:
            self.__opstartcodes=bestand.readline()
        if self.__opstartcodes != self.usb:
            print("foute opstartcodes!!!!!")
            quit()

class Scanner:
    def __init__(self):
        pass

class Stemcomputer:
    def __init__(self):
        pass

class Chipkaart:
    def __init__(self):
        pass

class USBStick:
    def __init__(self):
        with open("opstartcodes.txt", "r") as bestand:
            self.__opstartcodes=bestand.readline()
    
    def getOpstart(self):
        return self.__opstartcodes

#test voor kiezer klasse
#oKiezer1=Kiezer(1)
#print(oKiezer1)

def main():
    count=0
    randomgetallen=[]
    kiezers=[]
    kandidaten=[]
    stemmen=[]
    while len(randomgetallen)<=50:
        randomgetal=math.floor(random.random()*1200)
        if randomgetal not in randomgetallen:
            randomgetallen.append(randomgetal)


    Denver_Nuggets=Lijst("Denver_Nuggets")
    LA_Lakers=Lijst("LA_Lakers")
    Chicago_Bulls=Lijst("Chicago_Bulls")
    Miami_Heat=Lijst("Miami_Heat")
    Dallas_Mavericks=Lijst("Dallas_Mavericks")

    for x in range(0, 1200):
        if x in randomgetallen:
            oKandidaat1=Kandidaat(x)
            if count < 10:
                Denver_Nuggets.add_Kandidaat(oKandidaat1)
            elif count >= 10 and count < 20:
                LA_Lakers.add_Kandidaat(oKandidaat1)
            elif count >= 20 and count < 30:
                Chicago_Bulls.add_Kandidaat(oKandidaat1)
            elif count >= 30 and count < 40:
                Miami_Heat.add_Kandidaat(oKandidaat1)
            else:
                Dallas_Mavericks.add_Kandidaat(oKandidaat1)
            count+=1
            kandidaten.append(oKandidaat1)
        else:
            kiezers.append(Kiezer(x))
    
    oUSB1=USBStick()
    ostembus1=Stembus(oUSB1)
    
    print(randomgetallen)
    print(Denver_Nuggets)   
    print(LA_Lakers)
    print(Chicago_Bulls)
    print(Miami_Heat)
    print(Dallas_Mavericks) 
    #print(kiezers)



if __name__=="__main__":
    main()