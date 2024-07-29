# Compression/huffman.py
import heapq
from collections import defaultdict
import pickle

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

class HuffmanCompressor:
    def __init__(self):
        self.arbol = None

    def compress(self, data):
        arbol_huffman = ArbolHuffman(data)
        codificaciones = arbol_huffman.generar_codificacion_huffman()
        texto_codificado = arbol_huffman.codificar_texto(codificaciones)
        # Convertir la cadena de bits en un bytearray
        texto_comprimido = self.bits_to_bytearray(texto_codificado)
        return texto_comprimido, arbol_huffman

    def bits_to_bytearray(self, bits):
        b = bytearray()
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            b.append(int(byte, 2))
        return b

class ArbolHuffman:
    def __init__(self, data):
        self.data = data
        self.arbol_huffman = self.construir_arbol_huffman()

    def construir_arbol_huffman(self):
        frecuencias = defaultdict(int)
        for byte in self.data:
            frecuencias[byte] += 1

        cola_prioridad = [NodoHuffman(byte, frecuencia) for byte, frecuencia in frecuencias.items()]
        heapq.heapify(cola_prioridad)

        while len(cola_prioridad) > 1:
            nodo_izquierdo = heapq.heappop(cola_prioridad)
            nodo_derecho = heapq.heappop(cola_prioridad)

            nuevo_nodo = NodoHuffman(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
            nuevo_nodo.izquierda = nodo_izquierdo
            nuevo_nodo.derecha = nodo_derecho

            heapq.heappush(cola_prioridad, nuevo_nodo)

        return cola_prioridad[0]

    def generar_codificacion_huffman(self, nodo=None, codigo='', codificaciones={}):
        if nodo is None:
            nodo = self.arbol_huffman
        if nodo.caracter is not None:
            codificaciones[nodo.caracter] = codigo
        else:
            self.generar_codificacion_huffman(nodo.izquierda, codigo + '0', codificaciones)
            self.generar_codificacion_huffman(nodo.derecha, codigo + '1', codificaciones)
        return codificaciones

    def codificar_texto(self, codificaciones):
        texto_codificado = ''
        for byte in self.data:
            texto_codificado += codificaciones[byte]
        return texto_codificado
