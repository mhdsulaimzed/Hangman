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
    if guess in secret_word:
        guesses.append(guess)

    else:
        turns_remaining -= 1
        guesses.append(guess)


    return guesses,turns_remaining,next




    
    



    
        
    
    


   















if  __name__ == "__main__":
    pass





