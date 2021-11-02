# This program was written by Lakshh Khatri in November 2019.
# This program converts a printed sudoku puzzle to a digitial version through making the user input the values 
# in a specific, simple manner, which is then processed by the code in order to map these values to the sudoku grid.


# This function creates the canvas.
def setup():
    fullScreen() 
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSjeapgN80fISSgcunJ94QVbvGrJ1GSYK-FPOlW-MsZspMGX1St"
    # Loading image from a web server
    global webImg
    webImg = loadImage(url, "png")



def draw():
    command = input("This program will allow you to convert a written sudoku into a tif file \n You will be asked to enter 9 rows. Indicate the numbers 1-9 by simply typing the number. When moving to the next item in the row, do not click space. \n Input '-' to indicate a blank cell. For example, your first of 9 inputs for the 9 rows would look like: '12-68-5-9' \n TYPE 'yes' to start converting!")
    
    if command == 'yes':
        background(255,255,255)
        image(webImg, 250 , 0 ,900,900)
        
        sudoku_values = []
        
        count = 1
        
        for i in range(9): 
            user_input_line = input("Input row number " + str(count) + " : ") # Taking the user's inputs
            
            row = []
            
            while len(user_input_line) != 9: # checking if the user did in fact input 9 values
                user_input_line = input("You did not input 9 values. Input row number " + str(count) + " again: ")
    
            change = input("This is  what you inputted for row number " + str(count) + " '" + user_input_line +"'. If it is incorrect, and you'd like to change it, please type 'change'. If not just click enter.")
    
            while change == 'change': # allowing user to change his input
                user_input_line = input( "Input row number " + str(count) + " again: ")
        
                while len(user_input_line) != 9: # checking if the changed input is 9 characters long
                    user_input_line = input("You did not input 9 values. Input row number " + str(count) + " again: ")
        
                change = input("This is what you inputted for row number " + str(count) + " '" + user_input_line +"'. If it is incorrect, and you'd like to change it, please type 'change'. If not just click enter.")
            
            for cell_value in user_input_line:
                if cell_value == "-": # converting the '-' 's which represent a blank space, to an actual blank space " ".
                    row.append(" ")
                else:
                    row.append(cell_value)
                    
            sudoku_values.append(row)
            count += 1
            
        
        positions = []
        
        ending = 75 
        # generating the positions of the 81 squares in the sudoku grid.
        row1 = [(int(str(i) + str(ending)),100) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),100) for i in range(6,11)]
        row2 = [(int(str(i) + str(ending)),195) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),195) for i in range(6,11)]
        row3 = [(int(str(i) + str(ending)),290) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),290) for i in range(6,11)]
        row4 = [(int(str(i) + str(ending)),390) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),390) for i in range(6,11)]
        row5 = [(int(str(i) + str(ending)),485) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),485) for i in range(6,11)]
        row6 = [(int(str(i) + str(ending)),580) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),580) for i in range(6,11)]
        row7 = [(int(str(i) + str(ending)),683) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),683) for i in range(6,11)]
        row8 = [(int(str(i) + str(ending)),777) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),777) for i in range(6,11)]
        row9 = [(int(str(i) + str(ending)),874) for i in range(2,6)] + [(int(str(i) + str(ending - 10)),874) for i in range(6,11)]
        
        positions.append(row1)
        positions.append(row2)
        positions.append(row3)
        positions.append(row4)
        positions.append(row5)
        positions.append(row6)
        positions.append(row7)
        positions.append(row8)
        positions.append(row9)    
    
        # This function draws the user's inputted values to their respective positions.
        def drawer(row,cell): 
            text(sudoku_values[row][cell],positions[row][cell][0], positions[row][cell][1]) # printing 
    
        # setting the font size to 100, and the color to black
        fill(50)
        textSize(100)
        
        for row in range(9): 
            for cell in range(9):
                drawer(row,cell) # passing in the indexes to access the value and position of all 81 squares to the drawer function
                
        save(input("Save your puzzle. Give it a name. If you do not wish to save, simply click enter without typing. The file will not be created."))    
        noLoop()
        
# Processing doesn't allow you to use Python's inbuilt 'input' function to get user input. 
# The function below rectifies this problem. It was taken from the user 'villares'
# in this processing forum: https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
