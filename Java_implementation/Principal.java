import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class Principal {

    private static String	HOST = "127.0.0.1";
    private static int	PORT = 65432;

    public static void main(String[] arg) throws IOException, UnknownHostException, InterruptedException {

        View view = new View();
        Ruido ruido = new Ruido();
        Presentation pres = new Presentation();

        // User input
        String input = view.getUserInput();
        System.out.println("User input \n" + input);

        // Obtaining the binary ascii code of the user input
        String encode_input = pres.textToBinaryAscii(input);
        System.out.println("Encode user input \n" + encode_input);

        // choosing the algorithm to use
        String alg = view.algorithToUse();

        String response = "";

        if (alg.equals("HAM")) {
            EmisorHam emisorH = new EmisorHam(encode_input);
            response = emisorH.get_response();
            
            StringBuilder newResponse = new StringBuilder(response); 
            // modificación del mensaje
            response = ruido.genRuido(alg, newResponse.reverse().toString());
        }

        else if (alg.equals("CRC")) {
            EmisorCRC emisor = new EmisorCRC(encode_input);
            response = emisor.get_response();
            
            // modificación del mensaje
            response = ruido.genRuido(alg, response);
        }

        // socket management

        //ObjectOutputStream oos = null; //para serialized objects
		OutputStreamWriter writer = null;
        ObjectInputStream ois = null;
        System.out.println("Emisor Java Sockets\n");

        //crear socket/conexion
		Socket socketCliente = new Socket( InetAddress.getByName(HOST), PORT);

		//mandar data 
		System.out.println("Enviando Data\n");
		writer = new OutputStreamWriter(socketCliente.getOutputStream());

        // Algorithm to use
		writer.write(alg + "$");

		String payload = response;
		writer.write(payload);	//enviar payload
		Thread.sleep(100);

		//limpieza
		System.out.println("Liberando Sockets\n");
		writer.close();
		socketCliente.close();
    }
}
