import html
import os
import openpyxl
import datetime as dt
 
now = dt.datetime.now()
now = now.strftime("%Y%m%d_%H%M%S")

os.system("clear")

cantidadColumnas = 5
try:
    cantidadColumnas = int(input("Digite la cantidad de columnas: "))
except:
    pass

tabla = []
texto = []

print(f"Introduzca el texto a trasponer en {cantidadColumnas} columnas o introduzca !q en una nueva línea para terminar: ")
while True:
    linea = html.escape(input())
    if linea == "!q":
        break
    texto.append(linea)

i = 1
temporal = []
for data in texto:
    if(i <= cantidadColumnas):
        temporal.append(data)
        i = i + 1
    else:
        tabla.append(temporal)
        i = 2
        temporal = []
        temporal.append(data)

os.system("clear")

wb = openpyxl.Workbook()
ws = wb.active
for fila in tabla:
    ws.append(fila)

wb.save(f"{now}_datos.xlsx")

print("Archivo generado con éxito.")
    

