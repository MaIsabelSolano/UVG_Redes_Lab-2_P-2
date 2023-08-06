import java.util.ArrayList;

public class ReceptorCRC {

    View view = new View();

    ArrayList<Boolean> trama = new ArrayList<>();
    ArrayList<Boolean> result;

    ArrayList<Boolean> polinomio;

    public ReceptorCRC(String tramaS) {

        for (char c: tramaS.toCharArray()) {
            if (c == '1') trama.add(true);
            if (c == '0') trama.add(false);
        }

        // generate polinomio
        polinomio = new ArrayList<>();
        Boolean[] pol = {
            true, false, true, true, false, true, false, true, 
            false, false, false, true, false, true, false, true,
            false, false, false, false, true, true, true, false, 
            true, false, false, true, true, false, true, false
        };
        for (boolean b: pol) polinomio.add(b);

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

        System.out.println("\nResultado receptor");
        view.printTrama(actual);

    }

}
