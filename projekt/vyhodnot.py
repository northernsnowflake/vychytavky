import sys
# Program pro vkládání si tu klidně napiš, ale pak ho ulož do souboru zpracuj.py
pole = []

while True:
    pridavek = input('')
    pole.append(pridavek)
    if pole[-1] == '':
        break
print(pole)
