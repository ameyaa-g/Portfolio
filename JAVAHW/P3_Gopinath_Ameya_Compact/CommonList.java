import java.util.*;

/**
 * Write a description of class CommonList here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class CommonList
{
    // instance variables - replace the example below with your own
    public CommonList()
    {
        // initialise instance variables
       
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static void main (String args [])
    {
        ArrayList<Integer> numbers = new ArrayList <>(Arrays.asList (4,2,9,1,7));
        printList(numbers);
        ArrayList<Integer> num = new ArrayList();
        printList(num);
        randomList(5,1,9);
    }
    
    public static void printList(ArrayList<Integer> list){
        System.out.print("[");
        for(Integer n : list){

            System.out.print(n + " ");
           }
        System.out.print("]");
    }
    
    public static void randomList (int n, int a, int b){
        Random random = new Random();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(random.nextInt(b - a) + a);
        }
        
        System.out.println(result);
        

        
    }
}
