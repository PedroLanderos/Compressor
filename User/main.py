# User/main.py
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
    ruta_guardado = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
    return ruta_guardado

def main():
    ruta_archivo = obtener_ruta_archivo()
    if ruta_archivo:
        archive_handler = ArchiveHandler(ruta_archivo)
        texto_comprimido, tree = archive_handler.comprimir_archivo()  # Se espera que retorne un tuple
        if texto_comprimido:
            tamano_comprimido = len(texto_comprimido)  # texto_comprimido ya es un bytearray
            print("Tamaño del archivo comprimido:", tamano_comprimido, "bytes")

            ruta_guardado = obtener_ruta_guardado()
            if ruta_guardado:
                with open(ruta_guardado, 'wb') as file:  # Guardar directamente como binario
                    file.write(texto_comprimido)
                print("Archivo comprimido guardado en:", ruta_guardado)

if __name__ == "__main__":
    main()