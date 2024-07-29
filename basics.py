#get the archive, convert it to binary and make it only 0 and 1 and also at the same time separate it into bytes (blocks of 8 items) then save it as a string in a map to use the bucket strategy
#check the map structure and start building the tree with the same huffman logic
#save the archive into binary (replace the original with the binary one)
#to get the original archive, get the binary one into 0 and 1, and use the tree to re build it and save it as it original was (maybe save the archive type at the end of the string)

import tkinter as tk
from tkinter import filedialog
from sortedcontainers import SortedDict

class Node:
    def __init__(self):
        self.byte = None
        self.frequency = None
        self.left = None
        self.right = None

def SelectFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def ConvertToBinary(file):
    orderedBytes = {}  
    with open(file, "rb") as binaryFile:
        byte = binaryFile.read(1)
        while byte:
            byte = ord(byte)
            byte_binary = format(byte, '08b')  
            if byte_binary in orderedBytes:
                orderedBytes[byte_binary] += 1
            else:
                orderedBytes[byte_binary] = 1
            byte = binaryFile.read(1)
    sorted_byte_frequencies = sorted(orderedBytes.items(), key=lambda x: x[1])
    return sorted_byte_frequencies

def BuildTree(sortedByteFrequencies):
    #using the dictionary previously built
    current = -1;
    root = Node(None, None) #initializing the tree

    if root == None:
        sum = (sortedByteFrequencies[-1][1]) + (sortedByteFrequencies[-2][1]);
        root = Node();
    ##getting the last element and continue getting elements until the dictionary is empty 
    while(sortedByteFrequencies): #moving through the elements in the list
        hola = 10

def Main():
    bytesOrdered = ConvertToBinary(SelectFile())
    for aux, count in bytesOrdered:
        print(f"byte: {aux}, frecuencias: {count}")

if __name__ == "__main__":
    Main()