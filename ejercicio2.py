import pandas as pd

personal = [
    {"nombre": "Carlos", "turno": 1, "hora_ingreso": "06:02", "hora_salida": "14:08"},
    {"nombre": "Diana",  "turno": 2, "hora_ingreso": "14:05", "hora_salida": "22:11"},
    {"nombre": "Luis",   "turno": 1, "hora_ingreso": "06:15", "hora_salida": "14:20"},
    {"nombre": "María",  "turno": 2, "hora_ingreso": "14:00", "hora_salida": "22:05"},
    {"nombre": "Jorge",  "turno": 1, "hora_ingreso": "06:00", "hora_salida": "14:10"},
]

df = pd.DataFrame(personal)


print(df.head(3))

empleados_turno = df.groupby("turno").agg(
	empleados = ("nombre","count")
)
print(empleados_turno)

df["horas_trabajadas"] = 8


turno2= df[df["turno"] == 2]
print(turno2)