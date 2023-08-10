import socket 
import csv
from receptorCRC import *
from receptorHam import *

HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost

PORT = 65432        # Puerto, capa de Transporte

message = ""
algorithm = ""

def main():
    algorithmd_CRC = []
    withError_CRC = []
    residuos_CRC = []

    iterations = 500

    # CRC-32 ______________________________
    
    for x in range(iterations):

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

        algorithmd_CRC.append(message)

        rec = ReceptorCRC(message)
        res = rec.get_final_results()
        if res != "":
            print(f"Mensaje final: {binary_ascii_to_text(res)}")

        if (rec.detectedError()): withError_CRC.append("1")
        else: withError_CRC.append("0")

        residuos_CRC.append(rec.getResidue())

    with open("output/receptor_CRC.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Titles
        temp = ["id","alg_received", "err", "res"]
        csv_writer.writerow(temp)
        
        # Write the data to the CSV file row by row
        for i in range(iterations):
            al_ac = "'" + str(algorithmd_CRC[i]) + "'"
            we_ac = "'" + str(withError_CRC[i]) + "'"
            temp = [i, al_ac, we_ac, residuos_CRC[i]]
            csv_writer.writerow(temp)


    # Ham ______________________________

    algorithmd_Ham = []
    bitsAs_Ham = []
    reqs_Ham = []
    originals_Ham = []
    correccion_Ham = []
    responses_Ham = []

    for x in range(iterations):

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

        algorithmd_Ham.append(message)

        # Use Ham
        bitsA, req, orig = message.split(";")
        bitsAs_Ham.append(bitsA)
        reqs_Ham.append(req)
        originals_Ham.append(orig)

        Rec = ReceptorHam(req, bitsA)
        res, correcion = Rec.check()
        responses_Ham.append(res)
        correccion_Ham.append(correcion)

        print()
        print("Data enviada al receptor: ", req)
        print("\nResultado:", res)
        if correcion != "":
            print(f"Se hizo la correcion. Trama final: {orig}")
            print(f"Mensaje final: {binary_ascii_to_text(orig)}")
        else:
            print(orig)
            print(f"Mensaje final: {binary_ascii_to_text(orig)}")
        print()

    # Save to to csv
    with open("output/receptor_Ham.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Titles
        temp = ["id","alg_received", "bits", "reqs", "orig", "corr", "res"]
        csv_writer.writerow(temp)
        
        # Write the data to the CSV file row by row
        for i in range(iterations):
            al_ac = "'" + str(algorithmd_Ham[i]) + "'"
            bi_ac = "'" + str(bitsAs_Ham[i]) + "'"
            req_ac = "'" + str(reqs_Ham[i]) + "'"
            or_ac = "'" + str(originals_Ham[i]) + "'"
            co_ac = "'" + str(correccion_Ham[i]) + "'"
            res_ac = "'" + str(responses_Ham[i]) + "'"
            temp = [i, al_ac, bi_ac, req_ac, or_ac, co_ac, res_ac]
            csv_writer.writerow(temp)



        


if __name__ == '__main__':
    main()