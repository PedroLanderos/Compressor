import tkinter as tk
from tkinter import filedialog
import threading
import time

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def convert_to_binary(file):
    ordered_bytes = {}
    lock = threading.Lock()
    
    def count_frequencies(start, end):
        local_counts = {}
        with open(file, "rb") as binary_file:
            binary_file.seek(start)
            chunk = binary_file.read(end - start)
            for byte in chunk:
                byte_binary = format(byte, '08b')
                if byte_binary in local_counts:
                    local_counts[byte_binary] += 1
                else:
                    local_counts[byte_binary] = 1
        with lock:
            for byte, count in local_counts.items():
                if byte in ordered_bytes:
                    ordered_bytes[byte] += count
                else:
                    ordered_bytes[byte] = count
    
    num_threads = 8 # Ajustado a un número más razonable de hilos
    with open(file, "rb") as f:
        file_size = f.seek(0, 2)  # Mueve el puntero al final del archivo y obtiene la posición
    chunk_size = file_size // num_threads
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else file_size
        thread = threading.Thread(target=count_frequencies, args=(start, end))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    sorted_byte_frequencies = sorted(ordered_bytes.items(), key=lambda x: x[1])
    return sorted_byte_frequencies

def main():
    file_path = select_file()
    if file_path:
        start_time = time.time()
        bytes_ordered = convert_to_binary(file_path)
        end_time = time.time()
        for byte, count in bytes_ordered:
            print(f"byte: {byte}, frecuencias: {count}")
        print(f"Tiempo de ejecución: {end_time - start_time} segundos")

if __name__ == "__main__":
    main()
