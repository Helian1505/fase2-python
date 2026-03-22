#   Paso 1 - Crear DataFrame con Pandas

import pandas as pd

# Crear un DataFrame a partir de un diccionario

registros = [
    {"contenedor": "CONT001", "turno": 1, "skus": 1840, "dañados": 23},
    {"contenedor": "CONT002", "turno": 2, "skus": 2100, "dañados": 41},
    {"contenedor": "CONT003", "turno": 1, "skus": 950, "dañados": 8},
    {"contenedor": "CONT004", "turno": 2, "skus": 1760, "dañados": 35},
    {"contenedor": "CONT005", "turno": 1, "skus": 2200, "dañados": 19},
]

df = pd.DataFrame(registros)
print(df)

# Paso 2 - EXPLORAR EL DATAFRAME

# CUANTAS FILAS Y COLUMNAS TIENE
print(df.shape)

# las primeras filas - útil con datasets grandes
print(df.head(3))  # primeras 3 filas

# ultimas filas
print(df.tail(2))

# Información general del DataFrame
print(df.info())

# Estadísticas descriptivas de las columnas numéricas
print(df.describe())

# Nombres de las columnas

print(df.columns)

# tipos de datos de cada columna

print(df.dtypes)


# Paso 3 - Acceder a los datos

# Acceder a una columna completa
print(df["skus"])

# Acceder a varias columnas

print([["contenedor", "skus"]])

# Filtrar filas por condición

turno1 = df[df["turno"] == 1]
print(turno1)

# Filtrar con multiples condiciones
# & significa AND, | significa OR

filtro = df[(df["turno"] == 1) & (df["skus"] > 1000)]
print(filtro)

# Acceder a una fila por índice

print(df.iloc[0])  # primera fiila
print(df.iloc[-1])  # ultima fila

# Paso 4 - crear columnas nuevas

# Calcular el porcentaje de daño por contenedor
df["pct_daño"] = (df["dañados"] / df["skus"] * 100).round(2)

# Clasificar contenedores según nivel de daño
df["nivel_daño"] = df["pct_daño"].apply(lambda x: "alto" if x > 1.5 else "normal")

# El método .apply() con lambda aplica una función a cada fila de la columna. Léelo así: "para cada valor x en pct_daño, si es mayor a 1.5 es alto, si no es normal".

print(df)

# Paso 5 - Agregar y agrupar

# Métricas por turno - exactamente el dashboard de bodega

resumen_turno = (
    df.groupby("turno")
    .agg(
        total_skus=("skus", "sum"),
        total_dañados=("dañados", "sum"),
        contenedores=("contenedor", "count"),
    )
    .reset_index()
)

# calcular el porcentaje de daño por turno

resumen_turno["pct_daño"] = (
    resumen_turno["total_dañados"] / resumen_turno["total_skus"] * 100
).round(2)

print(resumen_turno)
