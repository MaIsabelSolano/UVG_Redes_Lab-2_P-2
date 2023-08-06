import java.util.ArrayList;
import java.util.Random;

public class EmisorCRC {

    Random rand = new Random();
    View view = new View();

    ArrayList<Boolean> trama = new ArrayList<>();
    ArrayList<Boolean> tramaOriginal;
    ArrayList<Boolean> polinomio;
    ArrayList<Boolean> result;

    public EmisorCRC(String input) {

        for (char c: input.toCharArray()) {
            if (c == '1') {
                trama.add(true);
            }
            else if (c == '0') trama.add(false);
        }

        // save a copy of the original before padding
        tramaOriginal = new ArrayList<>(trama);

        // Padding
        // while (trama.size() % 32 != 0 ) {
            for ( int i = 0; i < 31; i ++  ) {
                trama.add(false);
            }

        System.out.println("\ncon padding");
        view.printTrama(trama);

        // generate polinomio
        polinomio = new ArrayList<>();
        Boolean[] pol = {
            true, false, true, true, false, true, false, true, 
            false, false, false, true, false, true, false, true,
            false, false, false, false, true, true, true, false, 
            true, false, false, true, true, false, true, false
        };
        for (boolean b: pol) polinomio.add(b);

        System.out.println("\npolinomio");
        view.printTrama(polinomio);

        // excecute algorithm
        CRC();

    }

    private void CRC() {

        ArrayList<Boolean> actual = new ArrayList<>();

        // initialize by copying the first bits of the trama
        for (int i = 0; i < polinomio.size(); i++) {
            actual.add(trama.get(i) ^ polinomio.get(i));
        }
        System.out.println();
        view.printTrama(trama);
        view.printTrama(polinomio);
        view.printTrama(actual);

        int nextB = polinomio.size();

        while(nextB < trama.size()) {

            // remove the first 0 and add next bit
            
            actual.remove(0);
            actual.add(trama.get(nextB));
            nextB++;
            
            // check if the first digit is 0            
            if (actual.get(0)) {

                System.out.println();
                view.printTrama(actual);
                view.printTrama(polinomio);

                // oparate normally
                ArrayList<Boolean> temp = new ArrayList<>();
                for (int i = 0; i < polinomio.size(); i ++) {
                    temp.add(actual.get(i) ^ polinomio.get(i));
                }

                view.printTrama(temp);

                // replace
                actual = new ArrayList<>(temp);
            }

            else {
                System.out.println();
                view.printTrama(actual);
            }

        }

        System.out.println("\nResultado");
        result = new ArrayList<>(tramaOriginal);
        actual.remove(0); // remove first 0
        result.addAll(actual);
        view.printTrama(result);

    }

    public ArrayList<Boolean> getPolinomio() {
        return polinomio;
    }

    public String get_response() {
        String res = "";
        for (boolean b: result) {
            if (b) res += "1";
            else res += "0";
        }
        return res;
    }

    public boolean getParidad() {
        // Calculate paridad
        int cantOnes = 0;
        for (boolean b: trama) {
            if (b) cantOnes ++;
        }

        if (cantOnes % 2 == 0) return true;
        else return false;
    }
    
    
}
