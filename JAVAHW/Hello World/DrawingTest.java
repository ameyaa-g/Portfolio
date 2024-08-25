/* 
   This is a multi-line comment.  You can write notes here.
   And here...
   And here...
*/

import gpdraw.*;

public class DrawingTest {
    
    public static void main(String[] args) {

        // This is a single-line comment
        
        SketchPad paper;                 // declare a SketchPad variable
        DrawingTool pencil;              // declare a DrawingTool variable
  
        paper = new SketchPad(400,400);  // create the SketchPad
        pencil = new DrawingTool(paper); // create the DrawingTool
        
        pencil.down();                   // follow these commands to
        pencil.forward(100);             // draw the mystery shape
        pencil.turnRight(120);
        pencil.forward(100);
        pencil.turnRight(120);
        pencil.forward(100);
    }   
}