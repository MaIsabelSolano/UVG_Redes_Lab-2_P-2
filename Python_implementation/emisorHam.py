'''
    Universidad del Valle de Guatemala
    Redes de Computadora CC3067
    Grupo#11
    Laboratorio#2 PT.1
    Corrección de errores (Hamming)
'''

from prettytable import PrettyTable
import copy

class Emisor():
    def __init__(self, data):
        self.data = data
        self.cantBits = len(data)
    
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
        pars = {}
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
            
        newFC = copy.deepcopy(finalCheckVals)
            
        lastCheck = {}
        changeDic = {}
        for k,v in finalCheckVals.items():
            v2 = list(v.values())
            count = v2.count(1)
            change = 0
            if (count % 2 != 0):
                change = 1        
            
            for k2, v3 in v.items():
                if v3 == '+':
                    changeDic[k] = (k2,change)
                    v[k2] = change
                    n = {}
                    n[change] = v
                    pars[k] = n
                    
            lastCheck[k] = v
            
        for k,v in lastCheck.items():
            for k2, v2 in v.items():
                for k3,v3 in positions.items():
                    if k2 == k3 and v3 == '+':
                        positions[k3] = v2    
              
        # for k,v in lastCheck.items():
        #     print(k,v)
                        
        return "".join([str(x) for x in list(positions.values())])
