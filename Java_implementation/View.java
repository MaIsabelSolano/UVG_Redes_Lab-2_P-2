import java.util.ArrayList;
import java.util.Scanner;

public class View {

    Scanner scan = new Scanner(System.in);

    public View() {}

    public String getUserInput() {
        String input = "";
        boolean gettingInput = true;

        while (gettingInput) {
            System.out.print("Ingrese el mensaje que desea enviar: ");
            String Userinput = scan.nextLine();

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

    public String algorithToUse(){
        String option = "";

        while(true) {

            System.out.println("\nQué algoritmo desea utilizar para la transmisión (Escriba el número):");
            System.out.println("1) Hamming");
            System.out.println("2) CRC-32");

            option = scan.nextLine();
            
            if (option.equals("1")) return "HAM";
            else if (option.equals("2")) return "CRC";
            else System.out.println("\n[INPUT INVALIDO] Pruebe nuevamente\n");

        }

    }
    
}
