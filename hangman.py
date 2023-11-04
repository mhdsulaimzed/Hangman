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
    Word=get_masked_word(secret_word,guesses)
    guesses_sofar="".join(guesses)
    return f"""Word:{Word}   
           Turns remaining:{turns_remaining}
           Guessed so far:{guesses_sofar}      """
    

    
    




    
        
    
    


   















if  __name__ == "__main__":
    pass





