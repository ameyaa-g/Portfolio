import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.io.IOException;  // Import the IOException class to handle errors
import java.io.FileWriter; 

public class P3_Gopinath_Ameya_Compression{
    public static void compress(){
        try {
            File myObj = new File("LeetSpeak.java");
            Scanner myReader = new Scanner(myObj);
            FileWriter file = new FileWriter("P3_Gopinath_Ameya_LeetSpeak2.java"); 
            
            int count = 0;
            String line = myReader.nextLine();
            //file.write(count);
            
            while (myReader.hasNextLine()) {
                
                line.replaceAll("\t","  ");
                file.write(String.valueOf(count));
                
                file.write(line);
                file.write("\n");
                
                line = myReader.nextLine();
                if(line.contains("\t") ) {
                    for (int i = 0; i < line.length(); i++) {
                        if (line.charAt(i) == '\t') {
                            count++;
                        }
                    }
                    //count++;
                    file.write(count);
                    count = 0;
                }
                
            }
            
            myReader.close(); 
            file.close();
            
        
        } catch (FileNotFoundException e) {
              System.out.println("An error occurred.");
              e.printStackTrace();
            }
            catch (IOException o) {
              System.out.println("An error occurreddd.");
              o.printStackTrace();
            }
        }
    public static void main(String  args[]){
        compress();
    }
}
