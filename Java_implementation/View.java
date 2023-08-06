import java.util.ArrayList;
import java.util.Scanner;

public class View {

    Scanner scan = new Scanner(System.in);

    public View() {}

    public String getUserInput() {
        String input = "";
        boolean gettingInput = true;

        while (gettingInput) {
            System.out.print("Ingrese la secuencia a emitir: ");
            String Userinput = scan.nextLine();

            // check for other symbols other tha 0 or 1
            boolean invalidInput = false;
            for (char c: Userinput.toCharArray()) {
                if (c == '0' || c == '1') {
                    // correct
                } else invalidInput = true;
            }

            // check if the first symbol isn't 1
            if (Userinput.charAt(0) == '0') invalidInput = true;

            if (invalidInput){
                // The message contains symbols other than 0 or 1
                System.out.println("\n[INPUT INVALIDO] Pruebe nuevamente\n");
            } else {
                // Correct input

                System.out.println("Desea enviar " + Userinput + " al emisor?: (y/n)");
                String exit = scan.nextLine();

                if (exit.toLowerCase().equals("y")) {
                    // Exit the loop
                    input = Userinput;
                    gettingInput = false;
                } else if (exit.toLowerCase().equals("n")) {
                    System.out.println("Pruebe nuevamente");
                } else {
                    System.out.println("\n[INPUT INVALIDO] Pruebe nuevamente\n");
                }
            }
        }

        return input;
    }

    public void printTrama(ArrayList<Boolean> t) {
        String res = "";

        for(boolean b: t) {
            if (b) res += "1";
            else res += "0";
        }

        System.out.println(res);
    }
    
}
