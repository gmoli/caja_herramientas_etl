import csv

#ruta archivo entrada
input_file = 'template.csv'

#ruta archivo salida
output_file = 'template_mod.csv'

with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(csvfile, delimiter=';')
    writer = csv.writer(output_csv, delimiter=';')
    
    #Extrae encabezado y lo graba en la salida
    writer.writerow(next(reader))
    
    for row in reader:
        # completa la columna 3 con espacios hasta 200 caracteres, y encierra el campo con comillas simples
        col = row[2].strip("'")[:200].ljust(200)
        row[2] = f"'{col}'"
        # Escribir la fila modificada en el archivo de salida
        writer.writerow(row)

print("Proceso finalizado")
