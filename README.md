# vychytavky

Přesměrování do/ze souboru v příkazovém řádku
pokud vypisujete nějaké hodnoty v konzoli, můžete tento výstup přesměrovat do souboru
podobně můžete převzít vstup ze souboru pro funkci input
Pro přesměrování výstupu se využívá větší než (>).

C:\Projekt\Generator\generuj.py > vysledek.txt

Pro přesměrování vstupu se využívá menší než (<). Hodnota je jednom řádku je vstup pro input.

C:\Projekt\Vyhodnoceni\vyhodnot.py < vstupni_hodnoty.txt

Samostatný příklad (mimo Notebook)
vytvořte jednoduchý program na výpis hodnot (vytvořte seznam 10 jmen) a přidejte navíc prázdný řádek, který přesměrujete do souboru
po přesměrování do souboru zobrazte na sys.stderr hlášku, že je výstup dokončen
vytvořte další program, který bude přijímat vstup pomocí funkce input, hodnoty ukládat do pole a následně pole vytiskněte
do souboru přesměrujte vstup ze souboru z předchozího programu

------
použij příkazy

python generuj.py > vysledek.txt

python vyhodnot.py < vysledek.txt
