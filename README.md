#Tic-Tac-Toe
A simple game of Tic-Tac-Toe on the terminal. 

##Requirement
python 2.7

##To run code
```python app.py```

##Files description:
* app.py: main application file
* board.py: contains the game board class with supported functions
* interactions.py: contains human interactions
* ai.py: contains AI functions 

##Design
The code is divided into 4 parts according to functionality: a board class, a human player, an AI player, and the main function. 
###Board class
*file: board.py*

The board class contains the game array, and human, and AI symbols. It also contains getter and setter functions to modify the array. 
###Human player
*file: human.py*

This is implemented as a module. It contains function definitions pertaining to the human player. All interactions with the human player are defined in this module. 
###AI player
*file: ai.py*

This is implemented as a module. It contains all functions related to the AI player. The main algorithm for AI is implemented here. 
###Main application
*file: app.py*

This is the main function, which instantiates the board class, and runs the game. 

##AI algorithm:
1. Check if there is any possibility of AI winning. If yes, make entry and win, else goto 2
2. Check if there is any possibility of human winning. If yes, block it with the AI's assigned symbol. Else goto 3
3. Write into any available corners as they have higher influence. Else goto 4
4. See if center cell is empty. Fill it. Else goto 5
5. Fill any of the sides. 

##Developed with
1. Python 2.7
2. Virtualenv
3. grip: To preview markdown files in local browser
4. pep8: To check coding style

##Changes:
1. pip install nose
2. nosetests <filename.py> -vs