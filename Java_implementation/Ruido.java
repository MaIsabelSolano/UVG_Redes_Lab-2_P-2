import java.util.Random;

public class Ruido {
    
    public Ruido() {}

    public String genRuido(String alg, String trama) {
        String res = "";
        Random rand = new Random();

        if (alg.equals("CRC")) {
            int numRand = 0;
            for (char c: trama.toCharArray()) {
                numRand = rand.nextInt(1001);

                if (numRand == 375) {
                    // Realizar switch
                    if (c == '1') res += '0';
                    if (c == '0') res += '1';
                }

                res += c;
            }

            System.out.println("CRC ruido");
            System.out.println(trama);
            System.out.println(res);
        }

        else if (alg.equals("HAM")) {
            String[] sep = trama.split(";");
            int numRand = 0;
            for (char c: sep[0].toCharArray()) {
                numRand = rand.nextInt(100001);

                if (numRand == 375) {
                    // Realizar switch
                    if (c == '1') res += '0';
                    if (c == '0') res += '1';
                }

                res += c;
            }
            res += ";";
            for (char c: sep[1].toCharArray()) {
                numRand = rand.nextInt(10001);

                if (numRand == 375) {
                    // Realizar switch
                    if (c == '1') res += '0';
                    if (c == '0') res += '1';
                }

                res += c;
            }
            res += ";";
            for (char c: sep[2].toCharArray()) {
                res += c;
            }

            System.out.println("ham ruido");
            System.out.println(trama);
            System.out.println(res);

        }

        return res;
    }
}
