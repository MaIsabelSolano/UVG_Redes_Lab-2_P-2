public class Principal {
    public static void main(String[] arg) {

        View view = new View();
        StringToFile stf = new StringToFile();
        

        String input = view.getUserInput();
        System.out.println("user input \n" + input);

        // Give input to emisor
        EmisorCRC emisor = new EmisorCRC(input);
        String response = emisor.get_response();

        stf.createTextFile(response, "responseCRC");


        // ReceptorCRC receptor = new ReceptorCRC(response);
        System.out.println("\nCódigo de Hamming");
        EmisorHam emisorH = new EmisorHam(input);
        String[] n = emisorH.get_response().split(";");
        StringBuilder a = new StringBuilder(n[0]);
        String res = a.reverse().toString();
        System.out.println("Data enviada por el emisor: "+input);
        System.out.println("Respuesta del emisor: "+res+"\n");
        String resH = emisorH.get_response();
        StringBuilder stringBuilder = new StringBuilder(resH);
        String responseH = stringBuilder.reverse().toString();
        stf.createTextFile(responseH, "responseHamming");

    }
}
