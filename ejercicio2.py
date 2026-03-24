# Crea un DataFrame a partir de la lista de diccionarios "personal". Luego, realiza las siguientes operaciones:
# 1. Muestra las primeras filas del DataFrame.
import pandas as pd

personal = [
    {"nombre": "Carlos", "turno": 1, "hora_ingreso": "06:02", "hora_salida": "14:08"},
    {"nombre": "Diana", "turno": 2, "hora_ingreso": "14:05", "hora_salida": "22:11"},
    {"nombre": "Luis", "turno": 1, "hora_ingreso": "06:15", "hora_salida": "14:20"},
    {"nombre": "María", "turno": 2, "hora_ingreso": "14:00", "hora_salida": "22:05"},
    {"nombre": "Jorge", "turno": 1, "hora_ingreso": "06:00", "hora_salida": "14:10"},
]

df = pd.DataFrame(personal)

# Mostrar las primeras filas del DataFrame
print(df.head(3))

# Agrupar por turno y contar empleados en cada turno
empleados_turno = df.groupby("turno").agg(empleados=("nombre", "count"))
print(empleados_turno)

# Agregar una nueva columna con las horas trabajadas (asumiendo 8 horas por turno)
df["horas_trabajadas"] = 8

# Filtrar empleados del turno 2
turno2 = df[df["turno"] == 2]
print(turno2)
