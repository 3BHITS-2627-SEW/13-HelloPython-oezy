## Datei: pythonCheatSheet.py

## Dies ist ein kleines CHeat Sheet fuer die
## verwendung von Python fuer C und C++ programmierer

# Variable
#int eine Zahl = 43;
eineVariable = 13
print("eineVariable", eineVariable)
eineVariable = "blalala"
print("eineVariable:", eineVariable)

#Typisierung in Python: Ducktyping

# Daher: bitte immer nach Moeglichkeit typisieren
eineZweiteVariable : int = 14
print("eineZweiteVariable:", eineZweiteVariable**3)
eineZweiteVariable = "Text"
# erzeugt leider erste den Fehler zur Laufzeit!
#print("eineZweiteVariable:", eineZweiteVariable**3)

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)
eineVariable = 15

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)

# formatierte Aufgabe
# C: printf("Zahl lautet %i und ist Cool!", eineVariable);
#print("Zahl lautet %i \n und ist Cool!", eineVariable)
#formatierte Strings
einText = f"Zahl lautet {eineVariable**2} \n und ist Cool!"
alternativText = "Zahl lautet "+(eineVariable**2)+" \n und ist Cool!"
#Typ-Umwandeln
# (Type-Conversion)
einString = str((eineVariable**2))
alternativText = "Zahl lautet "+einString+" \n und ist Cool!"
print(einText)
print("Alternativ-Text:", alternativText)

# Eingabe von der Kommandozeile:
# int i=0;
# printf("Bitte geben Sie eine Zahl ein: ");
# scanf(&i);