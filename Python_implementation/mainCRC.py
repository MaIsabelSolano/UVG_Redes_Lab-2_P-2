from view import *
from emisorCRC import *
from receptorCRC import *

def main():
    
    # # Get user info
    # userInput = getUserInput()
    # print("Input")
    # print(userInput)

    # get input from file
    response = read_txt_file("responseCRC.txt")

    if response == "": 
        print("Error reading file")
        return

    
    # emisor = Emisor(userInput)
    response = response

    receptor = Receptor(response)

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
