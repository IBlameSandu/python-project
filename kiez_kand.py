import random
import math

#voornamen van de file ophalen en
#de \n weghalen
vn=[]
voornamen=open("textfiles/voornamen.txt", 'r')
data=voornamen.readlines()
vn.extend(name.strip('\n') for name in data)
voornamen.close()

#achternamen van de file ophalen en
#de \n weghalen
an=[]
achternamen=open("textfiles/achternamen.txt", 'r')
data=achternamen.readlines()
an.extend(name.strip('\n') for name in data)
achternamen.close()

class Kiezer:
    """Kiezer klasse, ze hebben een naam, leeftijd, aantal mogelijke stemmen,
    extra check op stemstatus (gestemd) en een rijksregisternr (onnodig)."""

    def __init__(self, id):
        self.__rijksregisternr=id
        self.__voornaam=random.choice(vn)
        self.__achternaam=random.choice(an)
        self.leeftijd=math.floor(random.random()*73)+18
        self.__mogelijkeStemmen=1
        self.__gestemd=False

    def getName(self):
        """Naam van de kiezers opvragen, reden: namen privé."""

        return f"{self.__voornaam} {self.__achternaam}"
    
    def gestemd(self):
        """Functie dat gebruikt wordt om aan te duiden dat een kiezer gestemd heeft,
        voor het geval dat een kiezer meer als 1 stem heeft zal deze de code stoppen."""

        self.__mogelijkeStemmen-=1
        self.__gestemd=True
        if(self.__mogelijkeStemmen!=0):
            print(f"kiezer {self.__voornaam} {self.__achternaam} is vals aan het spelen")
            exit()
    
    def heeftGestemd(self):
        """Functie dat de stemstatus returnt."""

        return self.__gestemd

    def __repr__(self):
        """Returnt de namen van de kiezers."""

        return f"{self.__voornaam} {self.__achternaam}"

class Kandidaat(Kiezer):
    """Kandidaat klasse dat voor een meerderheid werkt adhv overervingen van de kiezer klasse."""

    def __init__(self, id):
        super().__init__(id)
        self.__stemmen=0

    def stemOntvangen(self):
        """Een functie om ervoor te zorgen dat kandidaten stemmen kunnen ontvangen."""

        self.__stemmen+=1

    def getStemmen(self):
        """Functie om het aantal stemmen dat een kandidaat heef gekregen te returnen."""

        return self.__stemmen

class Lijst:
    """Lijsten gaan gewoon de partijen zijn, in elk lijst zullen
    er 10 kandidaten komen."""

    def __init__(self, naam):
        self.maxKandidaten=10
        self.naam=naam
        self.__kandidaten=[]

    def addKandidaat(self, kandidaat):
        """Kandidaat toevoegen aan het partij."""

        self.__kandidaten.append(kandidaat)
    
    def aantalKandidaten(self):
        """Het aantal kandidaten in een lijst returnen."""

        return len(self.__kandidaten)
    
    def getKandidaten(self):
        """Ik heb dit verkozen in plaats van een __repr__ functie, in het begin
        had ik beide, maar deze werd al doorheen mijn code gebruikt (en het werkt).
        Voor de rest heb ik geen nood ondervonden een __repr__ functie nog te hebben."""

        return self.__kandidaten