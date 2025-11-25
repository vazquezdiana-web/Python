import numpy as np
import pandas as pd

ventas = np.array([120, 95, 78, 110, 130, 125, 80, 60, 140, 150, 135, 100])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
df = pd.DataFrame({'Meses': meses, 'Ventas': ventas})
print(df)
print("Estadísticas de ventas:")
print(df['Ventas'].describe())
print("Mes con mayores ventas:", df.loc[df['Ventas'].idxmax()])
print("Mes con menores ventas:", df.loc[df['Ventas'].idxmin()])
media_ventas = df['Ventas'].mean()
df['Clasificación'] = np.where(df['Ventas'] >= media_ventas, 'Alta','Baja')
print("Clasificación de desempeño mensual:")
print(df)
resumen = df.groupby('Clasificación')['Ventas'].agg(['count', 'mean'])
print("Resumen por nivel de desempeño:")
print(resumen)