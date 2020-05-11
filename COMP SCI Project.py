# Yael Jakobov
#
# "I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus."
#
# My project is an interactive game that requires the player to get through the maze, and along the way the player will face obstacles. There are two ways to go through the maze, and end up at the end of the maze. Upon touching the obstacle a small window will pop up with a finance related question, which the player can chose to answer or skip, causing the obstacle to disappear, and allowing the player to move forward. 
 
import math # This is necessary for drawing the character, which uses the sin and cosine functions 
import Draw # This allows me to import functions and elements from the Draw file

Draw.setCanvasSize(900, 800) # Sets the board to go up to 900 on the x-axis and 800 on the y-axis
Draw.setBackground(Draw.BLACK) # Sets the background color of the maze to black 

keepPlaying = True # As long as this boolean term is True the player will be able to continue playing the game (further explaination later on in the code). 

# In order to make this a dynamic game, everytime the player moves the board needs to be redrawn. The board consists of a series of lines (with two x coordinates and two y coordinates), and different shapes. Therefore, I created a series of lists, and a series of loops, which will loop through the lists of lines and shapes with each move of the player to cause the board to be redrawn.  

# This lines list is a 2D list that contains all the coordinates for the lines that make up the maze. I hardwired the values of the coordinates of the lines because when the board is drawn, I want the lines to be between the same coordinates. 

lines = [
        [30, 60, 55, 60],
         [130, 60, 875, 60],
         [30, 60, 30, 750],
         [875, 60, 875, 750],
         [30, 750, 750, 750], 
         [815, 750, 875, 750],
         [95, 150, 380, 150],
         [380, 150, 380, 420],
         [380, 420, 650, 420],
         [650, 150, 800, 150],
         [800, 150, 800, 420],
         [650, 150, 650, 420],
         [520, 60, 520, 330],
         [30, 660, 150, 660],
         [150, 230, 150, 330],
         [150, 430, 150, 659],
         [815, 580, 815, 750] ,
         [750, 580, 750, 750], 
         [550, 580, 750, 580],
         [550, 580, 550, 680],
         [380, 680, 550, 680], 
         [380, 530, 380, 680],
         [30, 330, 150, 330],
         [530, 421, 530, 500],
         [290, 530, 380, 530],
         [290, 450, 290, 530],
         [220, 450, 290, 450],
         [220, 450, 220, 630],
         [220,630, 310, 630],
         [150, 330, 150, 330],
         [150, 230, 230, 230],
         [230, 230, 230, 360],
         [300, 310, 380, 310],
         [720, 420, 800, 420],
         [640, 650, 640, 750],
         [30, 530, 90, 530],
         [690, 510, 690, 580]
]

# This is a 2D list that contains the color, function, text and x and y coordinates that are necassary to draw the START and END signs everytime the board is redrawn. 

texts = [
    [Draw.WHITE, Draw.string, "START", 710, 770],
    [Draw.WHITE, Draw.string, "END", 50, 40]
]

# This function allows for one of the obstacles to be in the shape of a diamond. It takes x and y coordinates, and width and height as the parameters for the diamond's shape. 

def filledDiamond(x, y, width, height):
    coords = [x, y+height/2,
             x+width/2, y+height,
             x+width, y+height/2,
             x+width/2, y]
    Draw.filledPolygon(coords)
    
# The following variables contain the finance questions followed by their respective correct responses, which each correlate to one of the obstacles in the maze. Each question tells the user in what form they must respond as to streamline the process of removing an obstacle once the player has answered correctly.  

returnOnEquity = "If you invest $100 in Apple stock today and \
it is worth\n$250 at the end of the year, what is your return on equity?\
\n(answer format: decimal form)"

ansROE = 1.5

marketCap = "If there are 20,000 shares of Starbucks on the market \
\nat $100 per share, what is Starbucks's market \ncapitalization?\
\n(answer format: whole number)"

ansMC = 2000000

earningsPerShare = "If Google's net income is $900 billion, and it \
has \n300 billion outstanding shares, what is Google's EPS?\
\n(answer format: whole number)"

ansEPS = 3 

firmValue = "If the value of the J.A.K. firm is $250 million, and \
the value \nof its equity is $185 million, what is the value of its debt?\
\n(answer format: whole number)"

ansFV = 65 

priceEarnings = "If Costco is currently trading at $150 per share \
and its \nearnings over the past year were $5 per share, what is its \nP/E \
ratio?\n(answer format: whole number) "

ansPE = 30

beta = "If Tesla's stock has a beta of 2, and the risk free rate is 5%\nand the market has a return \
of 15%, what is Tesla's \npercentage return?\n(answer format: whole number) "

ansB = 35

# This shapes list is a 2D list that contains the color, shape, x and y coordinates, height, width, finance question and respective answer for each obstacle. Everytime the board is redrawn there is a respective function that loops through the list to redraw the shapes.  

shapes = [
    [Draw.BLUE, Draw.filledOval, 475, 510, 60, 60, returnOnEquity, ansROE ],
    [Draw.RED, filledDiamond, 240, 255, 73, 73, marketCap, ansMC],
    [Draw.GREEN, Draw.filledOval, 560, 215, 60, 60, earningsPerShare, ansEPS],
    [Draw.YELLOW, Draw.filledOval, 100, 75, 60, 60, firmValue, ansFV],
    [Draw.MAGENTA, Draw.filledRect, 420, 105, 60, 80, priceEarnings, ansPE],
    [Draw.CYAN, Draw.filledRect, 755, 450, 70, 70, beta, ansB]
]

# This function checks if the player has intersected the obstacle/shape. It takes as its parameter shape, which is a single list in the 2D shapes list cooresponding to all the elements of a specific shape. It checks if the player's (character) current x position and y position intersects the shape. It checks if the player's current x position is greater than the shape's x coordinate (represented by shape[2]) plus its width (represented by shape[4]). Or, if the player's x position and the character's width is less than the shape's x coordinate. Also, it checks if the player's current y position is less than the shape's y coordinate (represented by shape[3]) plus its height (represented by shape[5]). Or, if the player's y position and the character's height is less than the shape's y coordinate. If either statement holds true, the the function returns false and the value 0. Otherwise it returns the shape's respective finance quesion, and answer. 

def intersectsShape(shape):  
    if xPos > (shape[2] + shape[4]) or \
       (xPos + 50) < shape[2]:
        return (False, 0)
    elif yPos > (shape[3] + shape[5]) or \
       (yPos + 30) < shape[3]:
        return (False, 0)
    return (shape[6], shape[7])


# Both of the following functions checks if the player has intersected one of the maze's lines. The first funciton takes as its parameter line, which is a single list in the 2D shapes list cooresponding to the x and y coordinates of a line. It checks if the player's (character) current x position and y position intersects the line. It checks if the player's current x position is greater than the line's x coordinate (represented by line[0]) plus its width (represented by the absolute difference between the two x coordinates: line[0]- line[2]). Or, if the player's x position and the character's width is less than the line's x coordinate. Also, it checks if the player's current y position is less than the lines's y coordinate (represented by line[1]) plus its height (represented by the absolute difference between the two y coordinates: line[1] - ;ine[3]). Or, if the player's y position and the character's height is less than the lines's y coordinate. If either statement holds true, the the function returns false. Otherwise it returns true. The second function loops throught the entire 2D list of lines, and will return false or true depending on if the line intersected the maze. 

def intersectsLine(line): 
    if xPos > (line[0] + abs(line[0]-line[2])) or \
       (xPos + 50) < line[0]:
        return False
    elif yPos > (line[1] + abs(line[1]-line[3])) or \
       (yPos + 50) < line[1]:
        return False
    return True
  

def lineIntersects():
    for line in lines:
        if intersectsLine(line): 
            return True 
 
# This function creates the outer shape of the character. It takes x and y coordinates and width and height as its parameters.  

def filledRoundedRect(x, y, width, height):
    coords = [x, y+width/2,
             x, y+height+width/2,
             x+width, y+height+width/2, 
             x+width, y+width/2]
    for angle in range(0, 180, 10):
        rad = math.radians(angle)
        newx = math.cos(rad)*width/2
        newy = math.sin(rad)*width/2
        coords+= [x+width/2+newx, y+width/2-newy]
        
        Draw.filledPolygon(coords)
        
# This function calls on the filledRoundedRect to create the character's gray outline, and creates the character's eyes (which each have a blue circle inside a white circle). It take xPos and yPos as its parameters, which will change as the player goes through the maze causing the character to move. The xPos and yPos for the parts of the eyes are slightly bigger to ensure that the eyes will be in the top center of the character. 

def character(xPos, yPos):
    Draw.setColor(Draw.GRAY)
    filledRoundedRect(xPos, yPos, 50, 30)
    
    Draw.setColor(Draw.WHITE)
    Draw.filledOval(xPos+7, yPos+10, 15, 15)        
    Draw.setColor(Draw.BLUE)
    Draw.filledOval(xPos+12, yPos+15, 11, 11)
    
    Draw.setColor(Draw.WHITE)
    Draw.filledOval(xPos+24, yPos+10, 15, 15)
    Draw.setColor(Draw.BLUE)
    Draw.filledOval(xPos+29, yPos+15, 11, 11)

# This function is what causes the board to be redrawn everytime the player moves. It first clears the board, and then draws the character at its x and y position. It sets the color to white so that it can draw the lines of the maze. It loops through the 2D lines list, and goes through each single list and draws the line based on each list's coordinates. It then loops through the 2D list of shapes to draw each obstacle according to its designated shape, color and coordinates. Then, it loops through the 2D texts list to draw the START and END indications at their designated x and y coordinates and color.  

def redraw():
    
    Draw.clear()
    
    character(xPos,yPos)
    
    Draw.setColor(Draw.WHITE)
    for row in lines:
        Draw.line(row[0],row[1],row[2],row[3])    
    
    for shape in shapes:
        Draw.setColor(shape[0])
        shape[1](shape[2], shape[3], shape[4], shape[5])  
    
    for text in texts:
        Draw.setColor(text[0])
        text[1](text[2], text[3], text[4])
        
    Draw.show()
    
# This function returns the user's respons to the finance question that comes up once they intersect the shape. It takes no parameter, and sets up a variable called ans as an empty string. It contains a while loop that will continue looping as long as the character is typing something on the keyboard. If the player pressed a key on the keyboard, that key is assigned to the variable newKey. The function will concatenate the player's answer onto the empty ans string. Once the player presses the return key then the player's answer will appear on the board. If the player presses the '.' key it is converted from text (period) to the actual symbol ('.') This is necessary for when the answers to the finance questions are decimal answers. This function also sets the font size, color and x and y coordinates of where the text will appear on the shape that pop-ups with the finance question and the player's response. 

def getString():
        
        ans = ""
        
        while True:
            if Draw.hasNextKeyTyped():
                newKey = Draw.nextKeyTyped()
                if newKey == "Return":
                    return ans
                elif newKey == "period":
                    ans += "."
                else:
                    ans += newKey
            Draw.setFontSize(20)
            Draw.setColor(Draw.BLUE)
            Draw.string(ans, 310, 380)         
            Draw.show()

# This function draws the error box once the player's answer to the finance question was checked if it is incorrect. It begins by redrawing the board (because otherwise only the pop-up box with the error message will appear). It works by creating a new shape on the board that informs the player of his incorrrect response, and gives him the option of skipping the question or retrying. If the player choses to skip the question then the shape will be removed from the shapes list, and the the board will be redrawn (without that shape). If the player choses to try again, then the question will remain there. 

def wrongAns(question, answer):
    redraw()
    
    Draw.setColor(Draw.RED)
    sizeX = 520
    Draw.filledRect(175, 210, sizeX, 320)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(18)
    Draw.string("WRONG ANSWER \nto retry: enter R, to skip: enter S", 210, 280)
        
    curX = sizeX // 2
    curY = sizeX // 2
    size = 20
    
    response = getString().lower()
    if response == "r":
        popUp(question, answer)
    elif response == "s":
        for shape in shapes:
            if shape[6] == question:
                shapes.remove(shape)
        redraw()
    else:
        wrongAns(question, answer)
        
# This function is what pops-up the box with the shape's finance question. It sets up ans as the variable that contains the player's answer. Then the for loop goes through each shape in the shapes 2D list to check if it matches up with any of the answers (which are contained in shape[6]), then it will remove the shape from the list and then redraw the board (without that shape). Otherwise, the question will remain there (unless the player choses to skip it, as per the previous function). 

def popUp(question, answer):
    
    Draw.setColor(Draw.WHITE)
    sizeX = 520
    Draw.filledRect(175, 210, sizeX, 320)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(18)
    Draw.string(question, 210, 280)
    
    curX = sizeX // 2
    curY = sizeX // 2
    size = 20
    
    ans = getString()

    if ans == answer:
        for shape in shapes:
            if shape[6] == question:
                shapes.remove(shape)
        redraw()
    else:
        wrongAns(question, answer)
        
# This sets the character's initial x coordinate to 758, and its y coordinate to 740. This puts the character at the start of the maze. 

xPos = 758
yPos = 740

# This function gets called upon once the player has reached the end of the maze, and tells the player he has completed the maze and has the option to play again, or quit. If the player choses to play the game again, then the board gets redrawn with all the shapes. If the player choses to quit, then the box with the "YOU WON!!!" gets eliminated and the player is stil at the end of the game. If the player choses neither to continue or quit then the "YOU WON!!!" message will remain there.   

def youWon(): 
    
    Draw.setColor(Draw.YELLOW)
    sizeX = 520
    Draw.filledRect(175, 210, sizeX, 320)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(40)
    Draw.string("YOU WON!!!", 210, 280)
    Draw.setFontSize(18)
    Draw.string("Enter A to play again, enter Q to quit.", 210, 350)
    
     
    curX = sizeX // 2
    curY = sizeX // 2
    size = 20
    
    response = getString().lower()
    if response == "q":
        return False
    elif response == "a":
        return True
    else:
        youWon()
    
# So long as the player is still in the maze, (and the player has not reached the end of the maze and chose to qquit), then this while loop will continue looping. If this boolean expression is true, then the board will be redrawn. If the player has pressed a key then that key will get assigned to the variable newKey. The tempX and tempY variables were created as temporary variables and assigned with the character's current x and y position. This comes into play when the player presses a key (up, down, right or left) that will cause him to intersect one of the maze's lines; instead of letting the player move, the player will have to remain in his current position. However, in the case that it does not intersect a line then the player will be able to move in the direction they want (increments by 20). In addition, if the player intersects a shape, they will not be able to move. Rather, the obstacle's respective question will come up.     


while keepPlaying:
    
    redraw()
    
    if Draw.hasNextKeyTyped():
        nextKey = Draw.nextKeyTyped()
        tempX = xPos
        tempY = yPos

        if nextKey == "Right":
            xPos += 20
        elif nextKey == "Left":
            xPos -= 20
        elif nextKey == "Up": 
            yPos -= 20          # It's -20 because the player is beginning on the bottom of the board
        elif nextKey == "Down":
            yPos += 20
        
        if lineIntersects():
            xPos = tempX
            yPos = tempY

                 
    for shape in shapes:
        q, a = intersectsShape(shape) # This takes the shape's respective finance question and answer if the character intersected a shape. Otherwise, it will take False and 0 as its parameters, which will then never match up to the shape's finance question and answer, thereby never causing the shape to pop-up with the respective finance question(i.e. it will never call upon the popUp function).         
        if q:
            popUp(q, str(a))  
            
    if yPos < 40:  # This is where the maze ends and youWon() will be assigned to keepPlaying, to determine if the player wants to continue playing or to quit.  If the player choses to play again then the shapes list has to be recreated because some of the shapes were removed when the player answer or skipped the obstacle questions. It also reinstates the player's x and y positions to where the game begins. Otherwise, the "YOU WON!!" text box gets cleared and the board is redrawn, but the player remains at the end of the maze (could not let the playe completely quit the Draw module).  
        keepPlaying = youWon()
        if keepPlaying:
            shapes = [
                [Draw.BLUE, Draw.filledOval, 475, 510, 60, 60, returnOnEquity, ansROE ],
                [Draw.RED, filledDiamond, 240, 255, 73, 73, marketCap, ansMC],
                [Draw.GREEN, Draw.filledOval, 560, 215, 60, 60, earningsPerShare, ansEPS],
                [Draw.YELLOW, Draw.filledOval, 100, 75, 60, 60, firmValue, ansFV],
                [Draw.MAGENTA, Draw.filledRect, 420, 105, 60, 80, priceEarnings, ansPE],
                [Draw.CYAN, Draw.filledRect, 755, 450, 70, 70, beta, ansB]
            ] 
            xPos = 758
            yPos = 740
            redraw()
        else:
            Draw.clear()
            redraw()

            
            
            
           
        
            

            
            
            
        
            
        
    
            
    
           


    
    







  
  
    



                

                
                
            

    
    





