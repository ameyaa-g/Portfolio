public class DeckTester
{
    public static void main(String[] args) {
        Deck dec = new Deck();
        String[] symbols = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"};
        int[] values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

    for(int i=0;i<symbols.length; i++){
        Card card = new Card(symbols[i], values[i]);
        
        dec.add(card);
    }
    //dec.shuffle();
    for(int i=0;i<(dec.deckSize());i++){
        if (i < 5){
            dec.getCard(i).setFaceUp(true);
        }
        
    }
    //System.out.print(dec.toString());
    Deck playDeck = dec.cutDeck(0);
    System.out.print(playDeck);
    Deck draw = dec.cutDeck(1);
            
    for(int m=0;m<playDeck.deckSize();m++){
        
        String val = playDeck.getCard(m).toString();
        
        System.out.println(val);
    }
    System.out.println("end");
    for(int s=0;s<(draw.deckSize());s++){
        
        String va = draw.getCard(s).toString();
        
        System.out.println(va);
    }
    
    }
}
