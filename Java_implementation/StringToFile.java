import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class StringToFile {

    public StringToFile() {}

    public void createCSV(ArrayList<String> tramas, ArrayList<String> modified, ArrayList<String> noised, String fileName) {
        try {
            // Inicializar el buffer
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            for (int i = 0; i < tramas.size(); i++) {

                writer.write(tramas.get(i) + ","+ modified.get(i) + "," + noised.get(i) + "," +"\n");
            }

            writer.close();
            System.out.println("Archivo creado con éxito");
        } catch (IOException e) {
            System.err.println("Ha ocurrido un problema con la creación del archivo: " + e.getMessage());
        }
    }

}