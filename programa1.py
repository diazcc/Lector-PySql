import sys
import mysql.connector
from datetime import datetime

def guardarbd(archivo, num_lineas, num_palabras, num_caracteres):
    try:
        conex = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='datosdb'
        )
        cursor = conex.cursor()
        consultaSql = "INSERT INTO informacion (nombrearchivo, cantlineas, cantpalabras, cantcaracteres, fecharegistro) VALUES (%s, %s, %s, %s, %s)"
        datos = (archivo, num_lineas, num_palabras, num_caracteres, datetime.now())
        cursor.execute(consultaSql, datos)
        conex.commit()
        cursor.close()
        conex.close()
    except mysql.connector.Error as error:
        print(f"Ha habido un erro con la base de datos: {error}")

def contarLineas(archivo):
    num_lineas = 0
    num_palabras = 0
    num_caracteres = 0
    with open(archivo, 'r') as file:
        for linea in file:
            num_lineas =  num_lineas + 1
            num_palabras = num_palabras + len(linea.split())
            num_caracteres = num_caracteres + len(linea)
    return num_lineas, num_palabras, num_caracteres


if __name__ == "__main__":
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        num_lineas, num_palabras, num_caracteres = contarLineas(archivo)
        guardarbd(archivo, num_lineas, num_palabras, num_caracteres)
        print(f"Líneas: {num_lineas}")
        print(f"Palabras: {num_palabras}")
        print(f"Caracteres: {num_caracteres}")
