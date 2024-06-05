import random
import math



class Stembiljet:
    """Stembiljet klasse, het gaat de kiezer, lijstnr en kandidaatnr (index binnen lijst) krijgen van de stemcomputer."""

    def __init__(self, kiezer):
        """3 van de attributen maken sense, de controle attribuut is een extra om ervoor te zorgen dat de rgistratie iets veiliger 
        verloopt."""
        self.kiezer=kiezer
        self.__geregistreerd=False
        self.__controle=False
        
    def __registreer(self):
        """Om de registratie te voltooien."""

        if self.__controle:
            self.__geregistreerd=True
            #print("stembiljet geregistreerd")
    
    def controleer(self, scanner):
        """Om ervoor te zorgen dat als iemand toch op 1 of ander manier aan de scanner komt er extra checks in place zijn
        voor de veiligheid. Dit was niet een verplicht deel, maar als een CSC student vond ik het moeilijker maken voor extra
        veiligheid wel waard."""

        if scanner.getScan() and isinstance(scanner, Scanner):
            self.__controle=True
            self.__registreer()

    def registratieCheck(self):
        """Geeft True of False terug, afhankelijk van de registratie."""
        return self.__geregistreerd



class Stembus:
    """Stembus klasse, het gat opstartcodes doorgeven."""

    def __init__(self):
        """Letterlijk 1 lijst om de stembiljetten bij te houden."""

        self.__stembiljetten=[]

    def geefCodeUSB(self, usb):
        """gaat een nummer van de txt file adhv random kiezen en hashen, wat dan als de opstartcode zal functioneren."""

        try:
            with open("textfiles/opstartcodes.txt", "r") as bestand:
                opstart=bestand.readlines()
                self.__opstartcodes=hash(opstart[math.floor(random.random()*10)].strip())
                usb.setOpstart(self.__opstartcodes)
        except FileNotFoundError:
            print("file (chip) niet gevonden")
            quit()

    def addStembil(self, stembil):
        """Stembiljet toevoegen aan de lijst. Als die niet geregistreerd is of niet een instantie van de klasse is zal het niet aan de lijst
        worden toegevoegd en de gebruiker wordt ervan geinformeerd."""

        if isinstance(stembil, Stembiljet) and  stembil.registratieCheck():
            self.__stembiljetten.append(stembil)
        else:
            print(f"stembiljet ongeldig of niet geregistreerd")



class Scanner:
    """Scanner klasse dat stembiljetten zal nakijken"""

    def __init__(self):
        """Initialisatie van de Scanner klasse, het bevat enkel 1 attribuut en dat is de scan attribuut."""

        self.__scan=False

    def check(self, stembil):
        """De check methode zal nakijken of het meegegeven stembiljet effectief een instantie van de Stembiljet klasse is.
        als dat is wordt de attribuut scan op true gezet, het wordt dan opgevraagd in een andere methode (en op false gezet) om ervoor
        te zorgen dat er iets meer veiligheid is."""
        if isinstance(stembil,Stembiljet):
            self.__scan=True
            stembil.controleer(self)
        
    def getScan(self):
        if self.__scan==True:
            self.__scan=False
            return not self.__scan
        else:
            print("je moest hier niet aan kunnen komen.")



class Stemcomputer:
    """Klasse van de stemcomputers, er zijn 3 nodig."""

    __stemGoed1=False 
    __stemGoed2=False
    __stemGoed3=False
    __gebruikteStemComputer=0 
    __count=0

    def __init__(self, opstartUSB):
        """Init van de stemcomputers, hier wordt de initialisatie gedaan en nagekeken of de opstartUSB een geldig opstartcode bevat."""

        self.initialiseerd=False
        self.__codes=[]
        self.__chipkaartCodes=[]

        try:
            with open("textfiles/opstartcodes.txt", "r") as bestand:
                opstart=bestand.readlines()
                for x in opstart:
                    self.__codes.append(hash(x.strip()))
                if opstartUSB.getOpstart() in self.__codes:
                    self.initialiseerd=True
                    #print("usb goed")
        except FileNotFoundError:
            print("file niet gevonden")
            quit()

        try:
            with open("textfiles/meerOpstartcodes.txt", "r") as bestand:
                opstart=bestand.readlines()
                for x in opstart:
                    self.__chipkaartCodes.append(hash(x.strip()))
        except FileNotFoundError:
            print("file (chip) niet gevonden")
            quit()
        

    def stemmen(self, kiezer, chip, lijsten):
        """Methode gebruikt om te stemmen, kijkt na of de stemcomputer geïnitialiseerd is,
        kiest dan een willekeurig lijst en kandidaat(en). Als de willekeurig nummer van de 
        kandidaat beland op 10 krijgt iedereen van de lijst een stem."""

        if self.initialiseerd and chip.getOpstart() in self.__chipkaartCodes:
            Stemcomputer.__count+=1
            keuzen=math.floor(random.random()*3)+1
            if Stemcomputer.__gebruikteStemComputer==0:
                Stemcomputer.__gebruikteStemComputer=math.floor(random.random()*3)+1
            for x in range(keuzen):
                gekozenLijst=math.floor(random.random()*5)+1
                kandidaat=math.floor(random.random()*10)+1

                if Stemcomputer.__count==Stemcomputer.__gebruikteStemComputer:
                    if kandidaat==10:
                        for value in lijsten[f"Partij{gekozenLijst}"].getKandidaten():
                            value.stemOntvangen()
                    else:
                        value=lijsten[f"Partij{gekozenLijst}"].getKandidaten()
                        value[kandidaat].stemOntvangen()

            match Stemcomputer.__count:
                case 1: 
                    Stemcomputer.__stemGoed1=True
                case 2: 
                    Stemcomputer.__stemGoed2=True
                case 3: 
                    Stemcomputer.__stemGoed3=True 
                    self.stemSucces(kiezer) #stemSucces confirmeren dan alles resetten
                    Stemcomputer.__count=0
                    Stemcomputer.__stemGoed1=False 
                    Stemcomputer.__stemGoed2=False
                    Stemcomputer.__stemGoed3=False
        else:
            print("stemcomputer nog niet geinitialiseerd")
            quit()

    def stemSucces(self, kiezer):
        """Dit is een functie dat aangroept wordt als stemmen een succes was, het verlaagd de attribuut 'mogelijkestemmen'
        van de kiezer tot 0, wat ervoor zorgt dat een kiezer enkel 1 keer kan stemmen."""

        if Stemcomputer.__stemGoed1 and Stemcomputer.__stemGoed2 and Stemcomputer.__stemGoed3:
            kiezer.gestemd()
    
    def geefStembil(self, kiezer):
        """De stemcomputers moeten een stembiljet maken, dus ik wou dit deel niet in mijn main zetten.
        Ik verkoos dus om het een aparte functie te maken, reden voor apartheid: return zou het geven aan de vorige functie
        in plaats van de main."""

        return Stembiljet(kiezer)



class Chipkaart:
    """Dit is de klasse van de chipkaarten, persoonlijk verstond ik hun gebruikt niet het best, dus ik heb ze
    gebruikt als een soort van 2de 'identifier' bij de 'stemcomputer' klasse."""

    def __init__(self):
        """Initialisatie van de chipkaart, aangezien een dit wordt gebruikt om te checken of een kiezer zou mogen stemmen
        heb ik verkozen het enkel 1 sttribuut te geven, namelijk opstartcodes."""

        try:
            with open("textfiles/meerOpstartcodes.txt", "r") as bestand:
                opstart=bestand.readlines()
                self.__opstartcodes=hash(opstart[math.floor(random.random()*10)].strip())
        except FileNotFoundError:
            print("file (chip) niet gevonden")
            quit()
    
    def getOpstart(self):
        """Aangezien opstartcodes een private attribuut is om het onveranderlijk te maken van 
        buitenaf heb ik een get methode gemaakt om ze te kunnen opvragen."""

        return self.__opstartcodes



class USBStick:
    """Dit en de 'Chipkaart' klasse zijn bijna kopieën van elkaar, het enige verschil is dat 
    deze ook een setter methode heeft aangezien er in de opdracht wordt gezegd dat USB's hun
    codes krijgen van de Stembus"""

    def __init__(self):
        """Initialisatie van de USBStick, bevat enkel de opstartcodes dis als 0 starten (later wordt ervoor gecheckt met een if aangezien
        0 een false zou geven)."""

        self.__opstartcodes=0

    def getOpstart(self):
        """Om de opstartcodes op te vragen, als het 0 is heeft het geen nieuwe opstartcodes gekregen waardoor dit 
        zich niet zal uitvoeren."""

        if self.__opstartcodes:
            return self.__opstartcodes
        else:
            print("iets is fout gegaan!")
            quit()
    
    def setOpstart(self, code):
        """Om de opstartcode van de stembus op te halen."""
        self.__opstartcodes=code