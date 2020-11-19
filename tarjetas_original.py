import csv
from random import shuffle
 
def tarjeta(pal, dict):
    for english in pal:
        res = input(f'Cual es la traducción de {english}: ')
        for word, palabra in dict.items(): 
            if(english == word):
                if(palabra == res):
                    print("La respuesta es correcta")
                else:
                    print(f'La respuesta correcta era: {palabra}')

palabras = []
traduccion = []

with open('Ankidroid.csv', "r") as File:  
    reader = csv.reader(File)
    for row in reader:
        english = row[2]
        spanish = row[3]
        palabras.append(english)
        traduccion.append(spanish)

diccionario = dict(zip(palabras, traduccion))
shuffle(palabras)
tarjeta(palabras, diccionario)