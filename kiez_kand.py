import random
import math

vn=[]
voornamen=open("textfiles/voornamen.txt", 'r')
data=voornamen.readlines()
vn.extend(name.strip('\n') for name in data)
voornamen.close()

an=[]
achternamen=open("textfiles/achternamen.txt", 'r')
data=achternamen.readlines()
an.extend(name.strip('\n') for name in data)
achternamen.close()

class Kiezer:
    def __init__(self, id):
        self.__rijksregisternr=id
        self.__voornaam=random.choice(vn)
        self.__achternaam=random.choice(an)
        self.leeftijd=math.floor(random.random()*73)+18
        self.__mogelijkeStemmen=1

    def getName(self):
        return f"{self.__voornaam} {self.__achternaam}"
    
    def getNr(self):
        return self.__rijksregisternr
    
    def gestemd(self):
        self.__mogelijkeStemmen-=1
        if(self.__mogelijkeStemmen!=0):
            print(f"kiezer {self.__voornaam} {self.__achternaam} is vals aan het spelen")
            exit()

    def __repr__(self):
        return f"{self.__voornaam} {self.__achternaam}"

class Kandidaat(Kiezer):
    def __init__(self, id):
        super().__init__(self, id)
        self.stemmen=0

    def stemOntvangen(self):
        self.stemmen+=1
        return f"kandidaat {self.__voornaam} {self.__achternaam} heeft een stem ontvangen"

    def __repr__(self):
        return f"{self.__voornaam} {self.__achternaam}"


class Lijst:
    def __init__(self, naam):
        self.maxKandidaten=10
        self.naam=naam
        self.__kandidaten=[]

    def add_Kandidaat(self, kandidaat):
        self.__kandidaten.append(kandidaat)
    
    def aantal_kandidaten(self):
        return len(self.__kandidaten)

    def __repr__(self):
        return f"{self.__kandidaten}"