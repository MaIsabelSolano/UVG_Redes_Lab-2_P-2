from view import *

class ReceptorCRC():

    def __init__(self, response) -> None:

        self.trama = []
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
            actual.append(self.trama[i] ^ self.polinomio[i])

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

        cambiado = False

        for b in actual:
            if b: cambiado = True

        if (not cambiado): print("\nMensaje enviado sin cambios\n")
        else: print("\nMensaje envaido con errores\n")

        
