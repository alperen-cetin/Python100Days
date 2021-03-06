import random

word_list = ["banana","mouse","elephant","Echidna","Earwig"]

word = random.choice(word_list)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




unchecked_word = []
u = "_"
checked_letters = "".split()
for x in word:
    unchecked_word += u

lives = 6
lose_state = False
win_state = False


while win_state == False and lose_state == False:
    guess_input = str(input("make a guess:\n")).lower()
    
        
    for x in range(len(word)):
        
        if guess_input == word[x]:
            unchecked_word[x] = guess_input # word[x]
            
        elif guess_input != x:
            pass
    
    if guess_input not in unchecked_word:  
        lives -= 1
        print(lives)
        if lives <= 0:
            lose_state = True
            print("You Lose")
    
    if lose_state != True:
        print(stages[-lives])
        print(unchecked_word)
        
    if "_" not in unchecked_word:
        win_state = True
        print("Congrats")
    
    


    
                  
    
    
        
            
            
 
    




