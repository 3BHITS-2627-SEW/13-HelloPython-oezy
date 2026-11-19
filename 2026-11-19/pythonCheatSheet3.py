#Fortsetzung in der Datei pythonCheatSheet3.py
#ausführen mit python pythonCheatSheet3.py

#die Haupt-Funktion:
#nicht zulässig: non-default-parameter NACH default parameter
#def main(einParameter : str = "nix", einZweiterParameter : str) -> None:
#korrekte Schreibweise:
#def main(einZweiterParameter : str , einParameter : str = "nix") -> None:
def main(einParameter : str = "nix", einZweiterParameter : str = "aNix") -> None:
    print("ein Python CheatSheet!")

    meineListe : list = ["eins", "zwei", "drei", "viele..."]

    #Ausgabe:
    print("Mein Parameter einParameter: ", einParameter)
    print(f"Mein Parameter einZweiterParameter:{einZweiterParameter+"!"}")

    # Werte an die Liste anfuegen
    meineListe.append("noch viel mehr ..")
    #die Liste anzeigen:
    print(meineListe)
    #Anzeige geht ganz einfach, Warum???
    # Testen mit meineKlasse, ob das auch so einfach geht

    # 0. Importiere die Bibliothek
    #SCHLECHTE IDEE: an dieser Stelle importieren
    from mein_paket.meineKlasse import MeineKlasse

    # 1. ein neues Objekt anlegen
    einObjekt = MeineKlasse()
    # 2. mit print ausgeben
    print(einObjekt)
    print(einObjekt, sep="\n")
    #print(einObjket, "BLABLA", sep="\n")

    #gib die Liste aus:
    print(*meineListe, sep=" - ")
    # * entpackt die Liste
    # und fuegt diese 1:1 als Parameter in
    # den Funktionsaufruf ein
    print("Das vierte Element ist:", meineListe[3], sep="\n")


#rufe die Haupt-Funktion:
if __name__ == "__main__":
    #Umgang mit den Default-Parametern

    main()
    main("schon etwas")
    main(einZweiterParameter="November")

    main(einZweiterParameter="November", einParameter="is no None")