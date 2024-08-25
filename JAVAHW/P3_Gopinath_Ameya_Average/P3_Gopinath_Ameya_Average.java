import java.util.*;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;

/**
 * Write a description of class P3_Gopinath_Ameya_Average here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class P3_Gopinath_Ameya_Average
{
    public static void main (String args[]){
        try{
            Scanner scan = new Scanner(new File("numbers.txt"));
            FileWriter file = new FileWriter(new File("output.txt"));   
            int sum = 0;
            int count= 0;
            while(scan.hasNext()) {
                int num = scan.nextInt();
                //System.out.print(num);
                sum = (num+sum);
                count++;
            } 
            String average = String.valueOf(sum/count);
            file.write(average,0,average.length());
            file.close();
        }catch(IOException i){  
        System.out.println("Error: " + i.getMessage());  
        }
        
             
    }
}
