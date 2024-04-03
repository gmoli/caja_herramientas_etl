# -*- coding: utf-8 -*-

import pandas as pd
import psycopg2

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password=""
)

#Ruta de archivo de entrada
archivo_csv = "/tmp/template.csv"

#Leer archivo csv, separado por ;
data = pd.read_csv(archivo_csv, delimiter=";")

# Obtener los nombres de las columnas del encabezado del CSV
columnas = data.columns.tolist()

# Nombre de la tabla en la base de datos
tabla_postgres = "table_00"

# Convertir DataFrame a una lista de tuplas
filas = [tuple(x) for x in data.to_numpy()]

cur = conn.cursor()

# Crear la tabla en PostgreSQL
# Usamos los nombres de las columnas del encabezado del csv para definir los campos de la tabla
column_def = ", ".join([f"{col} TEXT" for col in columnas])
create_table_query = f"CREATE TABLE IF NOT EXISTS {tabla_postgres} ({column_def});"
cur.execute(create_table_query)

# Insertar los datos en la tabla
cur.executemany(f"INSERT INTO {tabla_postgres} ({', '.join(columnas)}) VALUES ({', '.join(['%s'] * len(columnas))});", filas)

conn.commit()

cur.close()
conn.close()

print("Datos cargados correctamente")
