
/**
 * Write a description of class BoardTester here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class BoardTester
{
    public static void main(String args[]){
        Board board = new Board (4,2);
        
        board.printBoard();
        //board.makeMove("A",1,2);
        //board.printBoard();
        board.drawCards();
        board.drawCards();
        
        board.printBoard();
    }
}
