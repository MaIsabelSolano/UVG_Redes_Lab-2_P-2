def getUserInput():
    gettingInput = True
    userInput = ""

    while (gettingInput):
        print("Ingrese la secuencia a emitir: ")
        userInput = input()

        # check for symbols other thatn 0 or 1
        invalidInput = False
        for c in userInput:
            if (c == '0' or c == '1'):
                # correct
                pass
            else: invalidInput = True

        # check if the first symbos is not 1
        if (userInput[0] != '1'): invalidInput = True

        if (invalidInput):
            print("\n[INPUT INVALIDO] Pruebe nuevamente")

        else:
            # correct input, keep going

            print("Desea enviar "+ userInput + "cone el emisora al receptor (y/n)")
            exit = input() 

            if (exit.lower() == "y"):
                return userInput
            
            elif (exit.lower() == "n"):
                print("Intente nuevamente")

            else:
                print("\n[INPUT INVALIDO] Pruebe nuevamente")
    
def printTrama(t):
    res = ""
    for b in t:
        if (b): res += "1"
        if (not b): res += "0"
    print(res)
    
def binary_ascii_to_text(binary_ascii):
    text = ""
    for i in range(0, len(binary_ascii), 8):
        binary_char = binary_ascii[i:i + 8]
        ascii_value = int(binary_char, 2)
        text += chr(ascii_value)
    return text