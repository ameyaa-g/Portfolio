
import java.util.Stack;
import java.lang.Object;

public class Board
{   
    /* *** TO BE IMPLEMENTED IN ACTIVITY 4 *** */
    // Attributes
    Stack [] stacks;
    String[] symbols =  {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    Stack <Card> completed = new Stack(); 
    
    
    int numStack;
    int numDeck;
    Deck draw;
    /**
     *  Sets up the Board and fills the stacks and draw pile from a Deck
     *  consisting of numDecks Decks.  Here are examples:
     *  
     *  # numDecks     #cards in overall Deck
     *      1          13 (all same suit)
     *      2          26 (all same suit)
     *      3          39 (all same suit)
     *      4          52 (all same suit)
     *      
     *  Once the overall Deck is built, it is shuffled and half the cards
     *  are placed as evenly as possible into the stacks.  The other half
     *  of the cards remain in the draw pile.
     */    
    public Board(int numStacks, int numDecks) {
        numStack = numStacks;
        numDeck = numDecks;
        //System.out.println(numStacks);
        
        
        int[] values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
        
        Deck deck = new Deck();
        for(int g =0;g<numDecks;g++){
            for(int m = 0; m<(numDecks*13); m++){
                if (m<13){
                    Card card = new Card(symbols[m],values [m]);
                    deck.add(card);
                }
            }   
        }
        deck.shuffle();
        Deck playDeck = deck.cutDeck(0);
        draw = deck.cutDeck(1);
        stacks = new Stack[numStacks];
        int stackSize = (numDecks*13)/(2*numStacks);
        int start = 0;
        for(int i=0;i<numStacks;i++){
            Stack<Card> stackk = new Stack();
            
                for(int f = 0; f<((stackSize));f++){
                    Card val = playDeck.getCard(start);
                    start ++;
                    stackk.push(val);
                }
              
                
            
            stacks [i] = stackk;
        } 
        hideDeck();
    }
    /**
     *  Moves a run of cards from src to dest (if possible) and flips the
     *  next card if one is available.
     */
    public void makeMove(String symbol, int src, int dest) {
        
          int stackSize = (numDeck*13)/(2*numStack);
          int start = 0;
          Stack<Card> destStack = new Stack();
          Stack<Card> srcStack = new Stack();
          destStack = stacks[dest];
          srcStack = stacks[src];
          boolean flag = false;
        for (start = 0; srcStack.size()>= start; start++ ){
              if(srcStack.peek().toString().equals(symbol)){
                  destStack.push(srcStack.pop());
                  
                  stacks[dest] = destStack;
                  stacks[src] = srcStack;
                  flag = true;
              } else if (flag == true){
                  srcStack.push(destStack.pop());
              }
              else{
                  destStack.push(srcStack.pop()); 
                  start ++;
              }
        }
        if (destStack.isEmpty()==false){
            Card card = srcStack.pop();
            card.setFaceUp(true);
            if (destStack.isEmpty()==false){
                srcStack.push(card);
            }
        }else if (destStack.isEmpty() == true){
            System.out.println("Stack " +src+"is Empty");
        }
    }

    /** 
     *  Moves one card onto each stack, or as many as are available
     */
    public void drawCards() {
            int f = 0;
            
            if(f<draw.deckSize()){
                for (int s = 0; s<numStack;s++){
                Card card = draw.getCard(s);
                card.setFaceUp(true);
                Stack <Card> stackk= new Stack();
                stackk=stacks[s];
                
                stackk.push(card);
                stacks[s] = stackk;
                f++;
                int i = draw.getIndex(card);
                draw.takeCard(i);
            }
        }
        
        
    }

    /**
     *  Returns true if all stacks and the draw pile are all empty
     */ 
    public boolean isEmpty() {
        boolean flag = false;
        for (int s = 0; s<numStack;s++){
        Stack<Card> nstack= new Stack();
        nstack = stacks[s];
        if (nstack.isEmpty() && draw.deckEmpty()){
            flag = true;
        }
    }
        return flag;
    }

    /**
     *  If there is a run of A through K starting at the end of sourceStack
     *  then the run is removed from the game or placed into a completed
     *  stacks area.
     *  
     *  If there is not a run of A through K starting at the end of sourceStack
     *  then an invalid move message is displayed and the Board is not changed.
     */
    public void clear(int sourceStack) {
        
        
            int count = 0;
            Stack <Card> stackk = new Stack();
            stackk = stacks [sourceStack];
            int stackSize = stackk.size();
            for(int f = 0; f<13;f++){
               Card card = stackk.pop();
                if(card.toString() == symbols [f]){
                   count ++;
               }
               stackk.push(card);
              
            
            
            
        } 
        if (count == 13 ){
            Stack <Card> com = new Stack();
            com = stacks [sourceStack];
           for(int f = 0; f<13;f++){
            
            Card car = com.pop();
            completed.push(car);
        }
        }
    }
    public void hideDeck(){
        int stackSize = (numDeck*13)/(2*numStack);
        Stack<Card> stackk = new Stack();
        

        for (int f = 0; f<numStack;f++){
            stackk = stacks [f];
            for(int s = 0; s<stackk.size();s++){
                if(s >0 && s < (stackk.size()-1)){
                    Card card = stackk.pop();
                    card.setFaceUp(false);
                    stackk.push(card);
                }else if (s==(stackk.size()-1)){
                    Card card = stackk.pop();
                    card.setFaceUp(true);
                    stackk.push(card);
                }
            }
            stacks [f] = stackk;   
        }
    }
    /**
     * Prints the board to the terminal window by displaying the stacks, draw
     * pile, and done stacks (if you chose to have them)
     */
    public void printBoard() {
        //System.out.print(numStack);
        for (int f = 0; f<numStack;f++){
            
            Stack<Card> newStack = new Stack();

            newStack = stacks[f];
            
            System.out.print(f+" ");
            
            //for(int m=0;m<(numDeck*13/(2*numStack));m++){
                System.out.println(newStack.toString());
                
            //}
            
        }
        for (int f = 0; f<draw.deckSize();f++){
            
            System.out.print(draw.getCard(f));
        }
        for(int c = 0; c<completed.size(); c++){
            System.out.print(completed.pop().getSymbol());
        }
    }
}