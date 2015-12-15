#Tic-Tac-Toe
A simple game of Tic-Tac-Toe on the terminal. 


##Developed with
1. Python 2.7
2. Virtualenv
3. grip: To preview markdown files in local browser

##Developer environment
```
virtualenv venv
source venv/bin/activate
pip install grip
pip install pep8
python app.py
```
##Files description:
* app.py: main application file
* board.py: contains the game board data structure with supported functions
* interactions.py: contains human interactions
* ai.py: contains AI functions 

##AI algorithm:
1. Check if there is any possibility of AI winning. If yes, make entry and win, else goto 2
2. Check if there is any possibility of human winning. If yes, block it with the AI's assigned symbol. Else goto 3
3. Write into any available corners as they have higher influence. Else goto 4
4. See if center cell is empty. Fill it. Else goto 5
5. Fill any of the sides. 