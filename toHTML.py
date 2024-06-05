from airium import Airium

def parser(lijsten):
    """Neemt de lijsten van de main functie over en 'parst' ze door ze te verdelen 
    in 3 lists, namelijk de kandidaten, stemmen per kandidaat en stemmen per lijst."""
    kandidaten=[]
    aantalstemmen=[]
    aantalstemmenPerPartij=[]

    for lijst in lijsten.values():
        som=0
        for x in lijst.getKandidaten():
            kandidaten.append(x.getName())
            aantalstemmen.append(x.getStemmen())
            som+=x.getStemmen()
        aantalstemmenPerPartij.append(som)
    
    HTMLgen(kandidaten, aantalstemmen, aantalstemmenPerPartij)

def HTMLgen(kandidaten, stemmen, totalestemmen):
    winnaar=max(totalestemmen)
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.meta(charset="utf-8")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            a.link(href="style.css", rel="stylesheet")
            a.title(_t="Verkiezingen")

        with a.body():
            a.h1(_t="resultaten van de verkiezingen:")
            for keer in range(len(totalestemmen)):
                if totalestemmen[keer] == winnaar:
                    with a.div(klass="winnaar"):
                        a.h2(_t=f"resultaten lijst{keer+1}: {totalestemmen[keer]} stemmen")
                        with a.ul():
                            for x in range(10):
                                a.li(_t=f"{kandidaten[x+10*keer]}: {stemmen[x+10*keer]} stemmen")
                else:
                    with a.div(klass="niet_winnaar"):
                        a.h2(_t=f"resultaten lijst{keer+1}: {totalestemmen[keer]} stemmen")
                        with a.ul():
                            for x in range(10):
                                a.li(_t=f"{kandidaten[x+10*keer]}: {stemmen[x+10*keer]} stemmen")

    with open("forWeb/index.html", "w") as html:
        html.write(str(a))
    html.close()