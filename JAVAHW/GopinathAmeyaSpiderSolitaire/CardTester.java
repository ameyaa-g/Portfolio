
public class CardTester
{
    public static void main(String[] args) {
        Card car = new Card("K",9);
        Card card = new Card("Y",9);
        System.out.println(car.compareTo(card));
        System.out.println(car.getSymbol());
        card.setFaceUp(true);
        System.out.println(card.isFaceUp());
        car.setFaceUp(false);
        System.out.println(car.isFaceUp());
        System.out.println(card.toString());
        System.out.println(car.toString());
        System.out.println(card.getValue());
    }
}
