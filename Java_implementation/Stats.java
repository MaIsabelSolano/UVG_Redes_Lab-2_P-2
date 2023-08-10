import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Random;

public class Stats {

    private static String	HOST = "127.0.0.1";
    private static int	PORT = 65432;

    public static void main(String[] args) throws IOException, UnknownHostException, InterruptedException  {

        Random rand = new Random();

        int iterations = 100;
        String trama;
        ArrayList<String> tramas = new ArrayList<>();

        // tramas generation
        for (int i = 0; i < iterations; i ++) {

            // initialize empty array/trama 
            trama = "";

            // random number between 7 and 25
            for (int j = 0; j <= rand.nextInt(25) + 7; j ++) {

                if (rand.nextBoolean()) trama += "1";
                else trama += "0";

            }

            System.out.println(trama);
            tramas.add(trama);

        }

        // CRC-32

        EmisorCRC emisorCRC;

        ArrayList<String> algorithmd_CRC = new ArrayList<>();
        for (int i = 0; i < tramas.size(); i ++ ) {

            String temp = "";
            emisorCRC = new EmisorCRC(tramas.get(i));
            temp = emisorCRC.get_response();

            algorithmd_CRC.add(temp);

        }

        ArrayList<String> modified_CRC = new ArrayList<>();
        ArrayList<String> noisedTramas_CRC = new ArrayList<>();
        Ruido ruido = new Ruido();

        // tramas posible modification
        for (int i = 0; i < algorithmd_CRC.size(); i++) {
            
            String temp = algorithmd_CRC.get(i);
            temp = ruido.genRuido("CRC", temp);

            noisedTramas_CRC.add(temp);

            // check if it changed
            if (temp.equals(algorithmd_CRC.get(i))) {
                modified_CRC.add("0");
            } else modified_CRC.add("1");

        }

        // save to file
        StringToFile stf = new StringToFile();
        stf.createCSV(
            tramas, 
            algorithmd_CRC,
            modified_CRC,
            noisedTramas_CRC,
            "output/emisor_CRC.csv"
        );


        // socket management

        for (int i = 0; i < noisedTramas_CRC.size(); i++) {
            //ObjectOutputStream oos = null; //para serialized objects
            OutputStreamWriter writer = null;
            System.out.println("\nEmisor Java Sockets");

            //crear socket/conexion
            Socket socketCliente = new Socket( InetAddress.getByName(HOST), PORT);

            //mandar data 
            System.out.println("Enviando Data");
            writer = new OutputStreamWriter(socketCliente.getOutputStream());

            // Algorithm to use
            writer.write("CRCS" + "$");

            String payload = noisedTramas_CRC.get(i);
            writer.write(payload);	//enviar payload
            Thread.sleep(100);

            //limpieza
            System.out.println("Liberando Sockets");
            writer.close();
            socketCliente.close();
        }
        
    }

}