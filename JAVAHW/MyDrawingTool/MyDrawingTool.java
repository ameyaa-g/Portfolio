

import gpdraw.*;
//import java.awt.Color;
import java.awt.*;
import javafx.scene.input.*;

public class MyDrawingTool extends DrawingTool{
    private String style = STYLE_SOLID;
    
    public static final String STYLE_ZIG_ZAG = "ZIG_ZAG";
    public static final String STYLE_DOTTED = "DOTTED";
    public static final String STYLE_SOLID = "SOLID";
    
    public MyDrawingTool(){
        //Call the DrawingTool constructor that takes a SketchPad
        super(new SketchPad(500, 500, 0));
        getPadPanel.addMouseListener(this);
    }
    
    //no need to do this on paper.
    //if the class changes, this is easy way to find out. 
    //goes right above the method, below JavaDocs
    
    @Override
    public void fillCircle(double radius){
        
        // can get color as 'color' becuase color is a protected variable
        //Color origColor = color;
        Color origColor = getColor();
        fillRect(2*radius,2*radius); 
        setColor(Color.WHITE);
        super.fillCircle(radius);
        //color = origColor;
        setColor(origColor);
    }
    //public void drawLine(double x, double y){
    // try to avoid changing protected to public, but you can.  
    //}
    //can't change class from subclass
    @Override
    protected void drawLine(double x, double y){
        if (style.equals(STYLE_ZIG_ZAG)){
            //draw a zig zag line
        }else if (style.equals(STYLE_DOTTED)){
            //draw a dotted line
        } else if (style.equals(STYLE_SOLID)){
            super.drawLine(50,50);
        }
    }
    
    public void moveTo(double x, double y){
        double dir = getDirection();
        boolean isPenDown = isDown();
        up();
        move(x, y);
        if (isPenDown) down();
        setDirection(dir);
    }
    
    /* Mouse Event Handlers */
    public void mouseClicked(MouseEvent e){
        moveTo(e.getX(),e.getY());
        super.fillCircle(10);
    }
    public void mouseEntered(MouseEvent e){
        
    }
    public void mouseExited(MouseEvent e){
        
    }
    public void mousePress(MouseEvent e){
        
    }
    public void mouseRelease(MouseEvent e){
        
    }
}


