from view import *

class Emisor():

    def __init__(self, userInfo):
        userInfo = userInfo

        self.trama = []

        for char in userInfo:
            if char == '1':
                self.trama.append(True)

            elif char == '0':
                self.trama.append(False)

        # Save a copy of the original before padding
        self.tramaOriginal = []
        for t in self.trama:
            self.tramaOriginal.append(t)

        # padding
        for i in range(31):
            self.trama.append(False)

        print("\ncon padding")
        printTrama(self.trama)


        # generate polinomio
        self.polinomio = [
            True, False, True, True, False, True, False, True, 
            False, False, False, True, False, True, False, True,
            False, False, False, False, True, True, True, False, 
            True, False, False, True, True, False, True, False
        ]

        self.CRC()

    def CRC(self):
        actual = []

        # Initialize actual
        for i in range(len(self.polinomio)):
            actual.append(self.trama[i] ^ self.polinomio[i])

        print()
        printTrama(self.trama)
        printTrama(self.polinomio)
        printTrama(actual)

        nextB = len(self.polinomio)

        while(nextB < len(self.trama)):

            # remove first 0 and add next value
            actual = actual[1:]
            actual.append(self.trama[nextB])
            nextB += 1

            # check if the first digit is 1
            if (actual[0]):

                print()
                printTrama(actual)
                printTrama(self.polinomio)

                temp = [actual[i] ^ self.polinomio[i] for i in range(len(self.polinomio))]

                printTrama(temp)

                actual = []
                actual = [x for x in temp]

            else:
                print()
                printTrama(actual)

        print("\nResultado emisor")
        self.result = [x for x in self.tramaOriginal]
        actual = actual[1:] # remove first 0
        for x in actual:
            self.result.append(x)
        printTrama(self.result)

    def get_response(self):
        res = ""

        for b in self.result:
            if (b): res += "1"
            else: res += "0"

        return res
        
    
        


        

        

        
        

    