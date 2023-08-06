'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from emisorHam import Emisor
from receptorHam import Receptor

def main():
    
    # get input from file
    input = read_txt_file("responseHamming.txt")

    if input == "": 
        print("Error reading file")
        return
    
    bitsA, req = input.split(";")

    newL = list(req)
    p = 2
    if newL[p] == '0':
        newL[p] = '1' 
    elif newL[p] == '1':
        newL[p] = '0'
    bad_request = "".join(newL)
    Rec = Receptor(bad_request, bitsA)
    res,correcion = Rec.check()

    print()
    print("Data enviada al receptor: ", req)
    print("Data modificada enviada al receptor: ", bad_request)
    print("\nResultado:", res)
    if correcion == "":
        print("Trama descartada por errores")
    else:
        print(correcion)
    print()

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("File not found.")
        return ""
    except IOError:
        print("Error reading the file.")
        return ""

if __name__ == '__main__':
    main()