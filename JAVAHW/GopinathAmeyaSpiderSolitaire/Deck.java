import java.util.ArrayList;
import java.util.Random;

public class Deck
{
    int numDeck;
    ArrayList<Card> deck;
    
    public Deck(){
        deck = new ArrayList();
    }
    public void shuffle(){
        Random rand = new Random();
        for (int i=0;i<deck.size();i++) {
        int r1 = rand.nextInt(deck.size()-i) + i;
        Card index= getCard(i);
        Card val = getCard(r1);
        replace(val,index);
        replace(index, val);
        
    }
    
    }
    @Override
    public String toString(){
        for(int i = 0;i<deck.size();i++ ){
            Card card = deck.get(i);
            return card.toString();
            
        }
        return "hi";
    }
    public Card getCard(int i){
        return deck.get(i);
    }
    public int getIndex(Card i){
        return deck.indexOf(i);
    }
    public int deckSize (){
        return deck.size();
    }
    public void add(Card c){
        deck.add(c);
    }
    public void replace(Card index, Card value){
        int inde = deck.indexOf(index);
        deck.set(inde, value); 
    }
    public Deck cutDeck(int index){
        Deck playDeck =new Deck();
        Deck draw = new Deck ();
        for (int i = 0; i< deck.size(); i++){
         if (i<(deck.size()/2)){
             Card car = deck.get(i);
             playDeck.add(car);
             
         }else if(i>(deck.size()/2)){
             Card cad = deck.get(i);
             draw.add(cad);
         }
        }
        Deck[] array = new Deck[ 2 ];
        array [0] = playDeck;
        array [1] = draw;
        return array[index];
        
    }
    public void takeCard(int i){
        deck.remove(i);
    }
    public boolean deckEmpty(){
        return deck.isEmpty();
    }
    public Deck takeTopCard(int n){
        Deck intdeck = new Deck();
        for (int m = n;m>=0; m++){
            takeCard(m);
            
        }
        return intdeck;
    }
    public void transferDeck(Deck otherdeck){
        for (int i = 0; i< deck.size(); i++){
            Card c = getCard(i);
            takeCard(i);
            otherdeck.add(c);
        }
    }
    
}
