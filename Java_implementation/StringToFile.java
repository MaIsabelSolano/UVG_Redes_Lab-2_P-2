import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class StringToFile {

    public StringToFile() {}

    public void createCSV(ArrayList<String> tramas, ArrayList<String> algorithm, ArrayList<String> modified, ArrayList<String> noised, String fileName) {
        try {
            // Inicializar el buffer
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            // titles
            writer.write("id,trama_og,codified,modified,w_noise\n");

            // content
            for (int i = 0; i < tramas.size(); i++) {

                writer.write(Integer.toString(i)+",'"+tramas.get(i) + "','" + algorithm.get(i) + "','" + noised.get(i) + "','" + modified.get(i) + "'\n");
            }

            writer.close();
            System.out.println("Archivo creado con éxito");
        } catch (IOException e) {
            System.err.println("Ha ocurrido un problema con la creación del archivo: " + e.getMessage());
        }
    }

}