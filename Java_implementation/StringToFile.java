import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class StringToFile {

    public StringToFile() {}

    public void createTextFile(String response, String fileName) {
        try {
            // Inicializar el buffer
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName + ".txt"));
            writer.write(response);
            writer.close();
            System.out.println("Archivo creado con éxito");
        } catch (IOException e) {
            System.err.println("Ha ocurrido un problema con la creación del archivo: " + e.getMessage());
        }
    }

}