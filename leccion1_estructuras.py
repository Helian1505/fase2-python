#              LISTAS
# Una lista es una secuencia de elementos en orden.
# Puede tener cualquier tipo de dato mezclado.

# Lista de SKUs en un contenedor
skus = ["A-001", "A-002", "A-003", "A-004"]

# Acceder a elementos - el indice empieza en 0
print(skus[0])  # A-001
print(skus[-1])  # A-004

# Agregar y quitar elementos

skus.append("A-005")  # Agrega al final de la lista
skus.remove("A-002")  # Elimina el elemento especificado
print(len(skus))  # Cantidad de elementos en la lista

# Recorrer una lista
for sku in skus:
    print(f"SKU: {sku}")


#             DICCIONARIOS
# Un diccionario es una colección de pares clave-valor.
# cada campo tiene un nombre (clave) y un valor asociado.

# Un registro de un contenedor

contenedor = {
    "id": "CONT004821",
    "fecha": "2025-03-15",
    "turno": 1,
    "skus_total": 1840,
    "skus_dañados": 23,
}

# Acceder a valores por clave
print(contenedor["id"])  # CONT004821
print(contenedor["skus_total"])  # 1840

# Agregar un campo nuevo
contenedor["porcentaje_daño"] = (
    contenedor["skus_dañados"] / contenedor["skus_total"] * 100
)
print(f"Daño: {contenedor['porcentaje_daño']:.2f}%")  # Daño: 1.25%

# Recorrer un diccionario

for campo, valor in contenedor.items():
    print(f"{campo}: {valor}")


#           Lista de diccionarios

# Esto es una tabla de datos en Python puro
# Cada diccionario es una fila, cada clave es una columna.


registros = [
    {"contenedor": "CONT001", "turno": 1, "skus": 1840, "dañados": 23},
    {"contenedor": "CONT002", "turno": 2, "skus": 2100, "dañados": 41},
    {"contenedor": "CONT003", "turno": 1, "skus": 950, "dañados": 8},
    {"contenedor": "CONT004", "turno": 2, "skus": 1760, "dañados": 35},
]

# Calcular el total de SKUs ingresados

total_skus = sum(r["skus"] for r in registros)
print(f"Total SKUs: {total_skus}")  # Total SKUs: 6650

# Filtrar registros del turno 1

turno1 = [r for r in registros if r["turno"] == 1]
print(f"Contenedores turno 1: {len(turno1)}")

# Contedor con más daños
max_daño = max(registros, key=lambda r: r["dañados"])
print(f"Mas daños: {max_daño['contenedor']} con {max_daño['dañados']} SKUs")


#             TUPLAS y conJUNTOS

# Tupla - como una lista pero inmutable (no se puede cambiar)
# se usa para datos que no deben modificarse

turnos_validos = (1, 2, 3)
coordenadas_bodega = (4.7110, -74.0721)  # latitud, longitud - no deben cambiar

# Conjunto (set) - colección sin duplicados
# Perfecto para encontrar valores únicos

skus_ingresados = ["A-001", "A-002", "A-001", "A-003", "A-002", "A-001"]
skus_unicos = set(skus_ingresados)
print(f"SKUs únicos: {skus_unicos}")  # SKUs únicos:
print(
    f"Duplicados eliminados: {len(skus_ingresados) - len(skus_unicos)}"
)  # Duplicados eliminados: 3
