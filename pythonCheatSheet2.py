# Fortsetzung des Cheat-Sheets
import numpy
import numpy as npy
from numpy import number as npynb
#importieren von bibliotheken
from numpy import *
# eigene Bibliotheken bzw. Pakete importieren
from mein_paket.meineKlasse import MeineKlasse

def main ():
    number1 = numpy.sqrt(4)
    print("Wurzel aus 4:", number1)
    number2 = npy.sqrt(16)
    print("Wurzel aus 16:", number2)

    #Verwende die eigene Klasse:
    #MeineKlasse
    meinObjekt = MeineKlasse()
    print("Name vom Objekt:", meinObjekt.name)
    pass

if __name__ == "__main__":
    main()