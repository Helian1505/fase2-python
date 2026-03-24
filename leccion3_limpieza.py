# Dataset sucio
import pandas as pd
import numpy as np

# Crear un DataFrame con datos sucios
datos_crudos = [
    {
        "contenedor": "CONT001",
        "turno": 1,
        "skus": 1840,
        "dañados": 23,
        "fecha": "2025-03-15",
    },
    {
        "contenedor": "CONT002",
        "turno": 2,
        "skus": 2100,
        "dañados": 41,
        "fecha": "15/03/2025",
    },
    {
        "contenedor": "CONT003",
        "turno": None,
        "skus": 950,
        "dañados": 8,
        "fecha": "2025-03-15",
    },
    {
        "contenedor": "CONT004",
        "turno": 2,
        "skus": None,
        "dañados": 35,
        "fecha": "2025-03-16",
    },
    {
        "contenedor": "CONT002",
        "turno": 2,
        "skus": 2100,
        "dañados": 41,
        "fecha": "15/03/2025",
    },
    {
        "contenedor": "CONT005",
        "turno": 1,
        "skus": -500,
        "dañados": 19,
        "fecha": "2025-03-16",
    },
    {
        "contenedor": "CONT006",
        "turno": 3,
        "skus": 1200,
        "dañados": None,
        "fecha": "2025-03-16",
    },
    {
        "contenedor": "cont007",
        "turno": 1,
        "skus": 1500,
        "dañados": 12,
        "fecha": "2025-03-17",
    },
    {
        "contenedor": "CONT008",
        "turno": 2,
        "skus": 99999,
        "dañados": 28,
        "fecha": "2025-03-17",
    },
]

df = pd.DataFrame(datos_crudos)
print("Dataset original:")
print(df)
print(f"\nForma: {df.shape}")

# Paso 1 - identificar los problemas
print("\--- DIAGNÓSTICO ---")

# valores nulos por columna
print("Valores nulos:")
print(df.isnull().sum())

# Duplicados
print(f"\nFilas duplicadas: {df.duplicated().sum()}")

# Estadisticas para detectar valores raros
print("\nEstadisticas:")
print(df.describe())

# Lo anterior es el diagnostico para entender los datos

# Paso 2 - Eliminar duplicados

print(f"\nAntes: {len(df)} filas")
df = df.drop_duplicates()

print(f"\nDespues de eliminar duplicados: {len(df)} filas")

# Paso 3 - Estandarizar texto
# cont007 esta en minúscula - estandarizar a mayúsculas

df["contenedor"] = df["contenedor"].str.upper().str.strip()
print("\nContenedores estandarizados:")
print(df["contenedor"])
# .str.upper() convierte a mayúsculas. .str.strip() elimina espacios al inicio y al final


# Paso 4 - estandarizar fechas

# Hay dos formatos: "2025-03-15" y "15/03/2025"
# pd.to_datetime con inferencia automática resuelve ambos

df["fecha"] = pd.to_datetime(df["fecha"], format="mixed", dayfirst=True)
print(f"\nFechas estandarizadas:")
print(df["fecha"])
print(f"Tipo de dato: {df['fecha'].dtype}")

# Paso 5 - Manejar valores nulos
# Los valores nulos son None o NaN. Tienes dos opciones: eliminar la fila o rellenar con un valor. La decisión depende del contexto de negocio.

print(f"\nNulos antes: {df.isnull().sum().sum()}")

# turno nulo - no sabemos de qué turno es, no podemos asumir
# decisión: eliminar esa fila

df = df.dropna(subset=["turno"])

# Dañados nuño - podemos asumir 0 daños si no se reportaron
df["dañados"] = df["dañados"].fillna(0)

# skus nulo- no podemos inventar este número, eliminamos la fila
df = df.dropna(subset=["skus"])


print(f"Nulos después: {df.isnull().sum().sum()}")
print(f"Filas restantes: {len(df)}")

# Paso 6 - Eliminar valores imposibles

# SKUs negativos son imposibles - error de sistema
print(f"\nFilas con skus negativos: {len(df[df['skus'] < 0])}")
df = df[df["skus"] > 0]

# 99999 SKUs en un contenedor es imposible - outlier extremo
# En el mundo real consultorías con el negocio antes de eliminar

print(f"Filas con skus > 5000: {len(df[df['skus'] > 5000])}")
df = df[df["skus"] <= 5000]

print(f"Filas después de limpiar imposibles: {len(df)}")

# Paso 7 - convertir tipos de datos

# Turno debe ser entero, no decimal
df["turno"] = df["turno"].astype(int)
df["dañados"] = df["dañados"].astype(int)

print(f"\nTipos de datos finales:")
print(df.dtypes)

# Paso 8 - El dataset limpio
df["skus"] = df["skus"].astype(int)
print("\n--- DATASET LIMPIO ---")
print(df)
print(f"\nResumen de limpieza:")
print(f"  Filas originales:  9")
print(f"  Filas finales:     {len(df)}")
print(f"  Filas eliminadas:  {9 - len(df)}")
