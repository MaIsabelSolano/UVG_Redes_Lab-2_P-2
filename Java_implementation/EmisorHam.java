import java.util.HashMap;

public class EmisorHam {

    String finalResponse = "";

    public EmisorHam(String input){
        System.out.println("");
        String originalData = input;
        int dataSize = originalData.length();
        int p = get_p(dataSize);
        int positions = dataSize + p;
        HashMap<Integer, String> positionsData = new HashMap<>();

        int[] powersOfTwo = new int[p + 1];
        for (int i = 0; i <= p; i++) {
            powersOfTwo[i] = (int) Math.pow(2, i);
        }

        int dataIndex = 0;
        for (int i = positions; i > 0; i--) {
            if (contains(powersOfTwo, i)) {
                positionsData.put(i, "");
            } else {
                positionsData.put(i, originalData.charAt(dataIndex) + "");
                dataIndex++;
            }
        }
        

        // Crear la tabla con las columnas p
        int[][] table = new int[positions + 1][p];
        for (int i = 0; i <= positions; i++) {
            for (int j = 0; j < p; j++) {
                int powerValue = powersOfTwo[j];
                table[i][j] = (i / powerValue) % 2;
            }
        }

        String bitsA = "";
        // Encontrar las posiciones n que poseen unos en cada columna p
        for (int j = 0; j < p; j++) {
            String onesPositions = "";
            for (int i = 0; i <= positions; i++) {
                if (table[i][j] == 1) {
                    onesPositions += i + " ";
                }
            }
            String[] positionsArray = onesPositions.trim().split(" ");
            int parityBit = 0;
            int count = 0;
            for (String positionStr : positionsArray) {
                int position = Integer.parseInt(positionStr);
                
                if(positionsData.get(position) != ""){
                    if (positionsData.get(position).equals("1")){
                        count++;
                    }
                }
            }

            if(count % 2 != 0){
                parityBit = 1;
            }

            for (String positionStr : positionsArray) {
                int position = Integer.parseInt(positionStr);
                
                if(positionsData.get(position) == ""){
                    positionsData.put(position, String.valueOf(parityBit));
                }
            }

            bitsA += parityBit;
        }

        StringBuilder finalString = new StringBuilder();
        for (String value : positionsData.values()) {
            finalString.append(value);
        }

        finalResponse = finalString.toString()+";"+bitsA;

    }

    private static boolean contains(int[] arr, int num) {
        for (int n : arr) {
            if (n == num) {
                return true;
            }
        }
        return false;
    }

    private int get_p(int dataSize){
        int p  = 1;
        while(p + dataSize + 1 > Math.pow(2,p)){
            p++;
        }
        return p;
    }

    public String get_response(){
        return finalResponse;
    }    
}
