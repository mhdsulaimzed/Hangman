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
    return random.choice(goodwords)

def get_masked_word(word,guesses):
    
    return len(word)*"-"


    
    




    
        
    
    


   















if  __name__ == "__main__":
    pass





