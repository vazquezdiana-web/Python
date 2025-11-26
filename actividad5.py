#Actividad 5: Creación de un reporte a partir de datos ficticios usando openpyxl para Excel y ReportLab para generar un archivo PDF.
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Ventas"

ws.append(["ID", "Vendedor", "Región", "Producto", "Cantidad", "Precio unitario"])

ventas = [
[1, "Ana", "Norte", "Laptop", 3, 15000],
[2, "Luis", "Sur", "Tablet", 5, 8000],
[3, "Karla", "Norte", "Monitor", 2, 3000],
[4, "Pedro", "Centro", "Laptop", 1, 15000],
[5, "Sofía", "Sur", "Teclado", 10, 500],
]

for fila in ventas:
    ws.append(fila)
    wb.save("ventas_semanales.xlsx")