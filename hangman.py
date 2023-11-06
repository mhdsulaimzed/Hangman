import random

def get_random_words(wordfile="/usr/share/dict/words"):

    goodwords=[]
    
    with open(wordfile) as w:
        words=[x.strip() for x in w]
        for i in words:
            if not i.islower():
                continue

            if not i.isalpha():
                continue

            if  len(i) <5:
                continue

            

            
            else:
                goodwords.append(i)
    
    secret_word=random.choice(goodwords)
    return secret_word

def get_masked_word(secret_word,guesses):

    masked_word=[]
    for i in secret_word:
        if i in guesses:
            masked_word.append(i)

        else:
            masked_word.append('-')
    
   
    return "".join(masked_word)

def get_status(secret_word,guesses,turns_remaining):
    word=get_masked_word(secret_word,guesses)
    guesses_sofar="".join(guesses)
    
    return f"""Word:{word} \n Guesses so far:{guesses_sofar} \n Turns remaining: {turns_remaining}  """
    

def play_game(secret_word,guesses,guess,turns_remaining):

    
    
    if guess in guesses:
        
        return guesses,turns_remaining,"next"
    guesses.append(guess)
    if "-" not in get_masked_word(secret_word,guesses):
        
        return guesses,turns_remaining,"game_won"

    if not guess in secret_word:
        turns_remaining -= 1

        if turns_remaining == 0:
            return guesses,turns_remaining,"game_over"
    
    return guesses,turns_remaining,"next"






# def main():
#     guesses=[]
#     turns_remaining=6
#     stages = [ 

        
         
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / 
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |      
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |     
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 """,
                
#                 """
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 """
#     ]

#     print("WELCOME TO HANGMAN")
#     print("---------------------------------------------------------------------------------------------------------- \n \n")
#     seceret_word=get_random_words()
#     print(seceret_word) 
    
#     while True:
#         print(stages[turns_remaining])
        
#         status=get_status(seceret_word,guesses,turns_remaining)
#         print(status)
#         guess=input("Guess a letter")

#         guesses,turns_remaining,action= play_game(seceret_word,guesses,guess,turns_remaining)

#         if action == "game_over":
#             print(f"OOps Gameover.... the word is {seceret_word}")
#             print(stages[turns_remaining])

#             break

#         if action == "game_won":
#             print(f"Congrats.. you win. the word is {seceret_word}")

#             next_round= input("For next word enter N/n  end to quit Q/q")

#             if next_round == "N" or next_round == "n":
#                 main()
#             if next_round == "q" or next_round == "Q":
#                 break








    










 
    
    



    
        
    
    


   















if  __name__ == "__main__":
    pass





