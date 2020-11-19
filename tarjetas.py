import csv
from random import shuffle
import app

def crear_tarjetas(option):
    palabras = []
    traduccion = []
    diccionario = {}

    with open('Ankidroid.csv', "r") as File:  
        reader = csv.reader(File)
        for row in reader:
            english = row[2]
            spanish = row[3]
            palabras.append(english)
            traduccion.append(spanish)

    diccionario = dict(zip(palabras, traduccion))
    if option == True:
        return diccionario
    else:
        return (palabras, traduccion)

def barajar_tarjetas(pal):
    shuffle(pal)
    return pal

"""def tarjeta(dict):
    for english in pal:
        for word, palabra in dict.items(): 
            if(english == word):
                if(palabra == app.res):
                    print("La respuesta es correcta")
                #else:
                    #print(f'La respuesta correcta era: {palabra}')"""

def tarjetas_ingles():
    palabras, traduccion = crear_tarjetas(0)
    english = barajar_tarjetas(palabras)
    for word in english:
        return word  

def english_to_spanish(res, word):
    diccionario = crear_tarjetas(1)
    for palabra, traduccion in diccionario.items():
        if(word == palabra):
            if(res == traduccion):
                return "La respuesta es correcta"
                #print("La respuesta es correcta")
            else:
                return f'La respuesta correcta era: {traduccion}'
                #print(f'La respuesta correcta era: {traduccion}') 
                #print(word, palabra, res, traduccion)

def tarjetas_español():
    palabras, traduccion = crear_tarjetas(0)
    spanish = barajar_tarjetas(traduccion)
    for palabra in spanish:
        return palabra  

def spanish_to_english(res, palabra):
    diccionario = crear_tarjetas(1)
    for word, traduccion in diccionario.items():
        if(traduccion == palabra):
            if(res == word):
                return("La respuesta es correcta")
            else:
                return(f'La respuesta correcta era: {word}') 
                #print(palabra, traduccion, word, res)


"""if __name__ == "__main__":
    diccionario = crear_tarjetas(1)
    print(diccionario)"""
    