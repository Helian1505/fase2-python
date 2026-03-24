import pandas as pd

personal_sucio = [
    {"nombre": "Carlos ", "turno": 1, "hora_ingreso": "06:02", "horas": 8},
    {"nombre": "diana", "turno": 2, "hora_ingreso": "14:05", "horas": 8},
    {"nombre": "Luis", "turno": 1, "hora_ingreso": "06:15", "horas": None},
    {"nombre": "María", "turno": 2, "hora_ingreso": "14:00", "horas": -3},
    {"nombre": "Jorge", "turno": 1, "hora_ingreso": "06:00", "horas": 8},
    {"nombre": "Carlos ", "turno": 1, "hora_ingreso": "06:02", "horas": 8},
    {"nombre": "PEDRO", "turno": 4, "hora_ingreso": "22:00", "horas": 8},
]

df = pd.DataFrame(personal_sucio)


# Eliminar duplicados

df = df.drop_duplicates()

# Estandarizar nombre

df["nombre"] = df["nombre"].str.strip().str.title()

# rellenar las horas nulas

df["horas"] = df["horas"].fillna(8)
df["horas"] = df["horas"].astype(int)

# Eliminar filas con horas negativas

df = df[df["horas"]>0]

# Elimina empleados con turno 4

df = df[df["turno"]!=4]

# Imprimir el dataset limpio

print(df)
