def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f_entrada, open(archivo_salida, 'w') as f_salida:
        first_line = True
        for linea in f_entrada:
            linea = linea.strip()
            #en la primera linea no quiero que inserte ","
            if first_line:
                linea_modificada = f"'{linea}'"
                first_line = False
            else:
                linea_modificada = f",'{linea}'"
		
            f_salida.write(linea_modificada + '\n')

if __name__ == "__main__":
    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    
    procesar_archivo(archivo_entrada, archivo_salida)
    
    print(f"El archivo {archivo_entrada} ha sido procesado. Los datos modificados se han guardado en {archivo_salida}.")
