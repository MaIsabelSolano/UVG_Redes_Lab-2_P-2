import socket 
import csv
from receptorCRC import *
from receptorHam import *

HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost

PORT = 65432        # Puerto, capa de Transporte

message = ""
algorithm = ""

def main():
    algorithmd = []
    withError = []
    residuos = []

    iterations = 100

    # CRC-32
    
    for x in range(100):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #bind reserva/asigna tal socket a una IP:puerto especifica
            s.bind((HOST, PORT))
            s.listen()
            #accept() bloquea y deja esperando
            conn, addr = s.accept()
            with conn:
                print(f"Conexion Entrante del proceso {addr}")
                while True: #en caso se envien mas de 1024 bytes
                    #recibir 1024 bytes
                    data = conn.recv(1024)
                    if not data:
                        break   #ya se recibio todo
                    # print(f"Recibido: \n{data!r}\n{data!s}\n{data!a}") #!r !s !a, repr() str() ascii()
                    ##echo
                    #conn.sendall(data)

                    temp = f"{data!s}"[2:][:-1].split('$')
                    algorithm = temp[0]
                    message = temp[1]
            
        print("obtenido")
        print(algorithm)
        print(message)

        algorithmd.append(message)


        # Use CRC-32
        rec = ReceptorCRC(message)
        res = rec.get_final_results()
        if res != "":
            print(f"Mensaje final: {binary_ascii_to_text(res)}")

        if (rec.detectedError): withError.append("1")
        else: withError.append("0")

        residuos.append(rec.getResidue())

    print(len(algorithm))
    print(len(withError))
    print(len(residuos))

    with open("output/receptor_CRC.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the data to the CSV file row by row
        for i in range(iterations):
            temp = [algorithmd[i], withError[i], residuos[i]]
            csv_writer.writerow(temp)


        


if __name__ == '__main__':
    main()