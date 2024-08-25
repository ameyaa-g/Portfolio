
/**
 * Write a description of class Student here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Student
{
    private int StudentId;
    private String Name;
    private static String school = "tisb";
    private static int p = 100;
    public int getId(){
        return StudentId;
    }
    public String getName(){
        return Name;
    }
    void display()
    {
        System.out.println("name"+ Name +"Roll no"+ StudentId+ "School"+school);
        System.out.println ("P"+ p);
    }
    Student(int i, String N)
    {
        StudentId = i;
        Name = N;
    }
    void changep()
    {
        p=p+1;
    }
    public static void main(String args[])
    {
        Student S1 = new Student (1,"ABC");
        Student S2 = new Student (2,"DDD");
        S1.display();
        S2.display();
        S1.changep();
        S2.changep();
        S1.display();
        S2.display();
    }
    public void setName (String N)
    {
        Name = N;
    }
    public void setId (int i)
    {
        StudentId = i;
    }
}
