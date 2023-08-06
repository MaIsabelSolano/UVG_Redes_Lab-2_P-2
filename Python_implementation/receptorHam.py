'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from prettytable import PrettyTable
import copy

class Receptor():
    def __init__(self, data, bitsA):
        self.originalDa = data
        self.data = data[:-3]
        self.cantBits = len(self.data)
        self.bitsA = bitsA
                
    def getP(self):
        p = 0
        isBigger = False
        while not isBigger:
            goal = 2**p
            check = p+self.cantBits+1
            if(goal >= check):
                isBigger = True
                return p
            p += 1
            
    def getPowers(self, p):
        powers = {}
        for i in range(p):
            powers[2**i] = f'P{i}'
        return powers
           
    def get_response(self):
        p = self.getP()
        bits = len(self.data)
        size = bits + p
        powers = self.getPowers(p)
        positions = {}
        for bit in range(size, 0, -1):
            if bit not in list(powers.keys()):
                positions[int(bit)] = '*'
            else:
                positions[int(bit)] = '+'
        dataV = list(self.data)
        dataV.reverse()
        for k,v in positions.items():
            if dataV:
                if v == '*':
                    val = dataV.pop()
                    positions[k] = int(val)
                else:
                    continue
        
        table = PrettyTable()
        valuesTable = {}
        n = [x for x in range(size+1)]
        table.add_column('n', n)
        for i in range(len(powers)):
            power = list(powers.keys())[i]
            name = powers[power]
            temp_column = [1 if (i // power) % 2 == 1 else 0 for i in range(size+1)]
            table.add_column(name, temp_column)
            valuesTable[name] = temp_column

        # Print tables
        self.table = table
        print(self.table)
        
        checkVals = {}
        for k,v in valuesTable.items():
            checkVals[k] = [indice for indice, valor in enumerate(v) if valor == 1]
        
        finalCheckVals = {}
        for k1,v1 in checkVals.items():
            temp = {}
            for el in v1:
                for k2,v2 in positions.items():
                    if el == k2:
                        temp[el] = v2
            finalCheckVals[k1] = temp

        self.newPos = {}
        for i in range(len(self.originalDa), 0, -1):
            self.newPos[i] = int(self.originalDa[::-1][i-1])
            
        for k,v in finalCheckVals.items():
            v2 = list(v.values())
            for k2, v3 in v.items():
                if k2 in self.newPos:
                    v[int(k2)] = self.newPos[k2]
                    
        bitsB = ""
        for k,v in finalCheckVals.items():
            count = 0
            for k2, v2 in v.items():
                if v2 == 1 and k2 in self.newPos:
                    count+=1

            if count % 2 == 0:
                bitsB += '0'
            else:
                bitsB += '1'

        bitsB = bitsB[::-1]
        return (self.bitsA, bitsB)
    
    def binario_a_decimal(self, numero_binario):
        numero_decimal = 0 

        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion

        return numero_decimal
    
    def check(self):

        bitsA, bitsB = self.get_response()
        if bitsA != bitsB and not all(elemento == '0' for elemento in list(bitsB)):
            decimal = self.binario_a_decimal(bitsB)
            return (f"Hubo un error en el bit {decimal}", f"Se hizo la correcion. Trama final: {self.toggle_char_at_position(decimal)}")
        return ("Todo correcto, el mensaje no cuenta con errores", "")
                
    def toggle_char_at_position(self, position):
        for k,v in self.newPos.items():
            if k == position:
                if v == 1:
                    self.newPos[k] = 0
                else:
                    self.newPos[k] = 1
                    
        result_string = ""
        for k,v in self.newPos.items():
            result_string += str(v)

        return result_string