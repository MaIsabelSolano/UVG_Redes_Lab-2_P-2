import socket 
from receptorCRC import *
from receptorHam import *

HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost

PORT = 65432        # Puerto, capa de Transporte

message = ""
algorithm = ""

def main():
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

    if (algorithm == "HAM"):
        # Use hamming
        bitsA, req = message.split(";")
        Rec = ReceptorHam(req, bitsA)
        res,correcion = Rec.check()

        print()
        print("Data enviada al receptor: ", req)
        print("\nResultado:", res)
        if correcion != "":
            print(f"Se hizo la correcion. Trama final: {correcion}")
            print(f"Mensaje final: {binary_ascii_to_text(correcion)}")
        else:
            print(req)
            print(f"Mensaje final: {binary_ascii_to_text(req)}")
        print()

    if (algorithm == "CRC"):
        # Use CRC-32
        rec = ReceptorCRC(message)
        res = rec.get_final_results()
        if res != "":
            print(f"Mensaje final: {binary_ascii_to_text(res)}")

if __name__ == '__main__':
    main()

