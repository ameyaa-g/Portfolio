
public class P3_Gopinath_Ameya_BacktoSchool
{
    public static void main (String args[]){
        Person bob =  new  Person("Coach Bob", 27, "M");  
        System.out.println(bob);

        Student lynne =  new  Student("Lynne Brooke", 16, "NB", "HS95129", 3.5);  
        System.out.println(lynne);

        Teacher mrJava =  new  Teacher("Duke Java", 34, "M", "Computer Science", 50000);  
        System.out.println(mrJava);

        CollegeStudent ima =  new  CollegeStudent("Ima Frosh", 18, "F", "UCB123",  
        4.0, 1, "English");  
        System.out.println(ima);
    }
}
class Person{
    private String myName ; // name of the person
    private int myAge; // person's age
    private String myGender; // "M" for male, "F" for female, "NB" for non-binary
    // constructor
    public Person(String name, int age, String gender){
        myName = name;
        myAge = age;
        myGender = gender;
    }
    public String getName(){
        return myName;
    }
    public int getAge(){
        return myAge;
    }
    public String getGender(){
        return myGender;
    }
    public void setName(String name){
        myName = name;
    }
    public void setAge(int age){
        myAge = age;
    }
    public void setGender(String gender){
        myGender = gender;
    }
    public String toString(){
        return myName + ", age: " + myAge + ", gender: " +
        myGender;
    }
}
class Student extends Person{
    private String myIdNum; // Student Id Number
    private double myGPA; // grade point average
    // constructor
    public Student(String name, int age, String gender,
        String idNum, double gpa){
        // use the super class' constructor
        super(name, age, gender);
        // initialize what's new to Student
        myIdNum = idNum;
        myGPA = gpa;
    }
    public String getIdNum(){
        return myIdNum;
    }
    public double getGPA(){
        return myGPA;
    }
    public void setIdNum(String idNum){
        myIdNum = idNum;
    }
    public void setGPA(double gpa){
        myGPA = gpa;
    }
    // overrides the toString method in the parent class
    public String toString(){
        return super.toString() + ", student id: " + myIdNum + ", gpa: " + myGPA;
    }
}
class Teacher extends Person{
    private String subject;
    private double salary;
    public Teacher(String name, int age, String gender, String mySubject,
    double mySalary){
        super(name, age, gender);
        subject=mySubject;
        
        salary=mySalary;
        
    }
    public String getSubject(){
       return subject; 
    }
    public double getSalary(){
        return salary;
    }
    public void setSubject(String subject){
        subject = subject;
    }
    public void setSalary(double salary){
        salary = salary;
    }
    public String toString(){
        return super.toString() + " subject: " +this.subject+ " salary: " +this.salary;
    }
}
class CollegeStudent extends Student
{
    private String major;
    private int year;
    public CollegeStudent(String name, int age, String gender,String myIdNum,double myGPA, int myYear, String myMajor)
    {
        super(name,age,gender,myIdNum, myGPA);
        major=myMajor;
        
        year = myYear;
    }
    public int getYear(){
        return year;
    }
    public String getMajor(){
        return major;
    }
    public void setYear(int year){
        year = year;
    }
    public void setMajor(String major){
        major = major;
    }
    public String toString(){
        return super.toString() + ", major: "+ major +", year: "+year;
    }
}
