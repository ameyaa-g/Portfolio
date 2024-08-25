
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;
import java.util.*;
class Student{
        int rollno;
        String name;
        int age;
        Student (int rollno,String name,int age){
            this.rollno=rollno;
            this.name=name;
            this.age=age;
            
        }
    
}
public class arraylist
{
    

    public static void main(String[] args)
    {
        Student S1 = new Student (222, "Aaaaah", 34);
        Student S2 = new Student (666, "Santa!", 200);
        
        ArrayList<Student> al = new ArrayList<Student>();
        
        al.add(S1);
        al.add(S2);
        
        System.out.println(al);
        
        //Iterator<Student> StudentIterator = al.iterator();
        for (String str:al)
        {
            
            System.out.println(al);
        }

    }
}

