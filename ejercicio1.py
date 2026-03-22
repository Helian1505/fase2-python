personal = [
    {"nombre": "Carlos", "turno": 1, "hora_ingreso": "06:02", "hora_salida": "14:08"},
    {"nombre": "Diana", "turno": 2, "hora_ingreso": "14:05", "hora_salida": "22:11"},
    {"nombre": "Luis", "turno": 1, "hora_ingreso": "06:15", "hora_salida": "14:20"},
    {"nombre": "María", "turno": 2, "hora_ingreso": "14:00", "hora_salida": "22:05"},
    {"nombre": "Jorge", "turno": 1, "hora_ingreso": "06:00", "hora_salida": "14:10"},
]

# [lo_que_quieres for elemento in lista if condición]

nombres_turno1 = [empleado["nombre"] for empleado in personal if empleado["turno"] == 1]
print(nombres_turno1)

cantidad_empleados = len(personal)
print(f"Cantidad de empleados:{cantidad_empleados}")

turnos_unicos = set(empleado["turno"] for empleado in personal)
print(f"Turnos únicos:{turnos_unicos}")

empleado_mas_temprano = min(personal, key=lambda e: e["hora_ingreso"])
print(
    f"El empleado que ingresó más temprano fue: {empleado_mas_temprano['nombre']} fue a las {empleado_mas_temprano['hora_ingreso']}"
)
