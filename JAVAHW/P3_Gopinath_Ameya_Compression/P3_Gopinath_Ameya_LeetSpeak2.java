0import java.util.Scanner;
0
0public class LeetSpeak {
0	
0	public static void main(String[] args) {
0		
0		Scanner in = new Scanner(System.in);
0		
0		System.out.print("Please enter a sentence in English > ");
0		String input = in.nextLine();
0		String output = "";
0		char nextChar = 0;
0		
0		// go through input and replace common characters
0		
0		for (int i = 0; i < input.length(); i++) {
0			
0			nextChar = input.charAt(i);
0			
0			switch (nextChar) {
0				
0				case 'o': case 'O': output += '0'; break;
0				case 'i': case 'I': output += '1'; break;
0				case 'z': case 'Z': output += '2'; break;
0				case 'e': case 'E': output += '3'; break;
0				case 'a': case 'A': output += '4'; break;
0				case 's': case 'S': output += '5'; break;
0				case 'g': case 'G': output += '6'; break;
0				case 't': case 'T': output += '7'; break;
0				case 'b': case 'B': output += '8'; break;
0				case 'p': case 'P': output += '9'; break;
0				default: output += nextChar;
0			}
0		}
0		
0		System.out.println("\n\nThe 1337 way to write your sentence is \"" +
0							output + "\"\n\n");
0	}	
