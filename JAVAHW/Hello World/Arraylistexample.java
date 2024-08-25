
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;
public class Arraylistexample
{
    

    public static void main(String[] args)
    {
        List<String> animals = new ArrayList<>();
        List<Integer> marks = new ArrayList<>();

        marks.add(12);
        marks.add(14);
        marks.add (23);
        
        System.out.println(marks);
        
        animals.add("Lion");
        animals.add("Tiger");
        animals.add("Flying squirrel");
        animals.add("doggo");
        animals.add("Flamingo");
        animals.add("Monkey");
        animals.add("DOnke");
        
        System.out.println(animals);
        
        animals.remove("Lion");
        System.out.println(animals);
        animals.remove(1);
        System.out.println(animals);
        Iterator<String> AnimalIterator = animals.iterator();
        while (AnimalIterator.hasNext())
        {
            String Animal = AnimalIterator.next();
            System.out.println(Animal);
        }
        
    }
}
