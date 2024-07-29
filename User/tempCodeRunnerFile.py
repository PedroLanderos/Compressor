import tkinter as tk
from tkinter import filedialog
import sys
import os

# Agregar el directorio del proyecto al sys.path
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)

from Middle.getArchive import ArchiveHandler

def obtener_ruta_archivo():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(title="Seleccione el archivo a comprimir")
    if ruta_archivo:
        print("Ruta del archivo seleccionado:", ruta_archivo)
        return ruta_archivo
    else:
        print("No se seleccionó ningún archivo.")
        return None

def obtener_ruta_guardado():
    root = tk.Tk()
    root.withdraw()
    ruta_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    return ruta_guardado

def main():
    ruta_archivo = obtener_ruta_archivo()
    if ruta_archivo:
        # Obtener tamaño del archivo original
        tamano_original = os.path.getsize(ruta_archivo)
        print("Tamaño del archivo original:", tamano_original, "bytes")

        archive_handler = ArchiveHandler(ruta_archivo)
        texto_comprimido = archive_handler.comprimir_archivo()
        if texto_comprimido:
            # Obtener tamaño del archivo comprimido
            tamano_comprimido = len(texto_comprimido.encode('utf-8'))
            print("Tamaño del archivo comprimido:", tamano_comprimido, "bytes")

            # Mostrar contenido del archivo original
            print("\nContenido del archivo original:")
            with open(ruta_archivo, 'r') as file:
                contenido_original = file.read()
                print(contenido_original)

            # Mostrar contenido del archivo comprimido
            print("\nContenido del archivo comprimido:")
            print(texto_comprimido)

            ruta_guardado = obtener_ruta_guardado()
            if ruta_guardado:
                with open(ruta_guardado, 'w', encoding='utf-8') as file:
                    file.write(texto_comprimido)
                print("Archivo comprimido guardado en:", ruta_guardado)

if __name__ == "__main__":
    main()
