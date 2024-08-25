
class Level
{
    // instance variables - replace the example below with your own
    int LevelNumber;
    int Basic;
    int DA;
    int HRA;
    int Medical;
    /**
     * Constructor for objects of class Level
     */
    public Level()
    {
        // initialise instance variables
        LevelNumber = 10;
        Basic = 10000;
        DA = 300;
        HRA = 2000;
        Medical = 30009;
    }
    public int getLevelNumber(){
        return LevelNumber;
    }
    public int getBasic(){
        return Basic;
    }
    public int getDA(){
        return DA;
    }
    public int getHRA(){
        return HRA;
    }
    public int getMedical(){
        return Medical;
    }
    public void setLevelNumber(int newLevelNumber){
        LevelNumber = newLevelNumber;
    }
    public void setBasic(int newBasic){
        Basic = newBasic;
    }
    public void setDA(int newDA){
        DA = newDA;
    }
    public void setHRA(int newHRA){
        HRA = newHRA;
    }
    public void setMedical(int newMedical){
        Medical = newMedical;
    }
}
public class Sampleprogram{
    
}
class employee{
    int ID;
    String Name;
    int NoOfLeaves;
    Level L;
    public employee(){
        ID = 0;
        NoOfLeaves = 0;
        L =new Level();
    }
    
    public float CalculateSalary(){
        float total;
        total = (L.getBasic()+L.getHRA()+L.getDA()+L.getMedical())-(L.getBasic()*NoOfLeaves);
        return total;
        
    }
    public boolean CompareSalary(employee e){
        if (e.CalculateSalary()<this.CalculateSalary())
            return true;
        else
            return false;
    }
}
class manager extends employee {
    int Allowance;
    public manager(){
        Allowance = 0;
    }
    public int getAllowance(){
        return Allowance;
    }
    public void setAllowance(int newAllowance){
        Allowance = newAllowance;
    }
    public float CalculateSalary(){
        float total;
        total = (L.getBasic()+L.getHRA()+L.getDA()+L.getMedical()+Allowance)-(L.getBasic()*NoOfLeaves);
        return total;
    }
}
class department{
    int noOfEmployees;
    int Array

}

