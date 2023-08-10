import java.util.ArrayList;
import java.util.Random;
import java.util.zip.CRC32;

public class Stats {

    public static void main(String[] args) {

        Random rand = new Random();

        int iterations = 100;
        String trama;
        ArrayList<String> tramas = new ArrayList<>();

        // tramas generation
        for (int i = 0; i <= iterations; i ++) {

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

        ArrayList<String> modified = new ArrayList<>();
        ArrayList<String> noisedTramas = new ArrayList<>();
        Ruido ruido = new Ruido();

        // tramas posible modification
        for (int i = 0; i < tramas.size(); i++) {
            
            String temp = tramas.get(i);
            temp = ruido.genRuido("CRC", temp);

            noisedTramas.add(temp);

            // check if it changed
            if (temp.equals(tramas.get(i))) {
                modified.add("0");
            } else modified.add("1");

        }

        // save to file
        StringToFile stf = new StringToFile();
        stf.createCSV(
            tramas, 
            modified,
            noisedTramas,
            "originales.csv"
        );
        
    }

}