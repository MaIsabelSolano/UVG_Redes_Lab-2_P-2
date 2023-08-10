from view import *

class ReceptorCRC():

    def __init__(self, response) -> None:

        self.trama = []
        self.res = False
        self.data = response
        for c in response:
            if (c == '1'): self.trama.append(True)
            elif (c == '0'): self.trama.append(False)
        # printTrama(self.trama)

        # generate polinomio
        self.polinomio = [
            True, False, True, True, False, True, False, True, 
            False, False, False, True, False, True, False, True,
            False, False, False, False, True, True, True, False, 
            True, False, False, True, True, False, True, False
        ]

        # printTrama(self.polinomio)

        self.CRC()

    def CRC(self):
        actual = []

        # Initialize actual
        for i in range(len(self.polinomio)):
            actual.append(self.trama[i])

        # print()
        # printTrama(self.trama)
        # printTrama(self.polinomio)
        # printTrama(actual)

        nextB = len(self.polinomio)

        while(nextB < len(self.trama)):

            # remove first 0 and add next value
            actual = actual[1:]
            actual.append(self.trama[nextB])
            nextB += 1

            # check if the first digit is 1
            if (actual[0]):

                # print()
                # printTrama(actual)
                # printTrama(self.polinomio)

                temp = [actual[i] ^ self.polinomio[i] for i in range(len(self.polinomio))]

                # printTrama(temp)

                actual = []
                actual = [x for x in temp]

            # else:
            #     # pasa los 0s
            #     print()
            #     printTrama(actual)

        print("\nResultado receptor")
        printTrama(actual)

        self.residue = actual

        self.cambiado = False

        for b in actual:
            if b: self.cambiado = True

        if (not self.cambiado): 
            print("\nMensaje enviado sin cambios\n")
            self.res = True
        else: 
            print("\nMensaje enviado con errores\n")

    def get_final_results(self):
        if self.res:
            return self.data[:-31]
        else:
            return ""
        
    def detectedError(self):
        if self.cambiado: return 1
        else: return 0
    
    def getResidue(self):

        res = "'"

        for x in self.residue:
            if x:
                res += "1"
            else: 
                res += "0"

        res += "'"

        return res

        
