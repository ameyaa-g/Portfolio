
/**
 * Write a description of class ex here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ex
{
    double power_1(int base, int n){
        double i = (n==0)? 1:power_1(base,n-1)*base;
        return i;
    }
    public static void main (String args[]){
        ex e = new ex();
        System.out.println(e.power_1(2,3));
    }
}
