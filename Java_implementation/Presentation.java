public class Presentation {

    public Presentation(){ }

    public String textToBinaryAscii(String text) {
        StringBuilder binaryAscii = new StringBuilder();
        
        for (char c : text.toCharArray()) {
            String binary = Integer.toBinaryString(c);
            binaryAscii.append(String.format("%08d", Integer.parseInt(binary))); // Pads with leading zeros
        }
        
        return binaryAscii.toString();
    }

    public String binaryAsciiToText(String binaryAscii) {
        StringBuilder text = new StringBuilder();
        
        for (int i = 0; i < binaryAscii.length(); i += 8) {
            String binaryChar = binaryAscii.substring(i, i + 8);
            int asciiValue = Integer.parseInt(binaryChar, 2);
            text.append((char) asciiValue);
        }
        
        return text.toString();
    }
}
