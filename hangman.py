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
global r_w  #random_word
r_w=get_random_words()




def masking_random_word(r_w):
    
    word_length=len(r_w)
    return "_"*word_length


r_w1="allan"
def user_input():
    guessed_letter=[]
    for i in range(0,6):
        input_letter=input("enter a letter")
        if input_letter in r_w1:



            
            guessed_letter.append(input_letter)
            print(guessed_letter)
            break

        else:




            
            guessed_letter.append(input_letter)

        
        
user_input()       
        
    
    


   















if  __name__ == "__main__":
    pass





