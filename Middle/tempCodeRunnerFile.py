class ArchiveHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def pass_to_compression(self):
        # Aquí deberías importar la función o clase de la capa compression que manejará la compresión
        # from compression import compressor
        # compressor.compress(self.file_path)

        # Simulación de llamada a la capa compression
        print(f"La ruta del archivo {self.file_path} se está pasando a la capa de compresión.")
