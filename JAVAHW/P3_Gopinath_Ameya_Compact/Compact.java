
import java.util.*;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;


public class Compact
{
    // ArrayList, loop, input every other thing in the array but a zero
    
    //For arrays, loop, remove zeros with if, count zeros, add them at the en
    public static void main(String args[])
    {
        File f =  new File("compact.txt");  
        ArrayList<Integer> arraylist = new ArrayList();
        
        int count = 0;
        int index = 0;
        int num = 0;
        int [] array = new int [100];
        try{
            Scanner in =  new Scanner(f); 
            //Scanner in2 =  new Scanner(f);
            
            
            while(in.hasNextInt()){
                int line = in.nextInt();
                arraylist.add(line);
                if (line == 0){
                    count ++;
                }else{
                    
                    array[index] = line;
                    index++; 
                }
                
            }
            for(int i=0;i<count;i++){
                array[index+i]=0;
            }
            
            in.close();
            System.out.println(arraylist);
            for(int i=0;i<array.length;i++){
            System.out.print(array[i]);
            }
        }catch(IOException i){
            System.out.println("Error: " + i.getMessage()); 
        }
        
    }

    
}
