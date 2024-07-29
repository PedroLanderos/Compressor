# Middle/getArchive.py
import sys
import os

# Agregar el directorio del proyecto al sys.path para poder importar desde Compression
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
compression_dir = os.path.join(project_dir, 'Compression')
sys.path.append(compression_dir)

from Compression.huffman import HuffmanCompressor

class ArchiveHandler:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.compressor = HuffmanCompressor()

    def comprimir_archivo(self):
        if self.ruta_archivo:
            with open(self.ruta_archivo, 'rb') as file:
                data = file.read()
            texto_comprimido, tree = self.compressor.compress(data)
            return texto_comprimido, tree
        else:
            print("No se proporcionó una ruta de archivo válida.")
            return None, None
